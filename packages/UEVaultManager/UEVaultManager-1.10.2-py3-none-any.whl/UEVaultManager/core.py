# coding=utf-8
"""
Implementation for:
- AppCore: handle most of the lower level interaction with the downloader, lfs, and api components to make writing CLI/GUI code easier and cleaner and avoid duplication.
"""
import concurrent
import json
import logging
import os
import shutil
import sys
import time
from base64 import b64decode
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from hashlib import sha1
from locale import getlocale, LC_CTYPE
from multiprocessing import Queue
from platform import system
from threading import current_thread, enumerate as thread_enumerate
from typing import Dict, List
from urllib.parse import urlparse

from requests import session
from requests.exceptions import ConnectionError, HTTPError

import UEVaultManager.tkgui.modules.globals as gui_g  # using the shortest variable name for globals for convenience
# noinspection PyPep8Naming
from UEVaultManager import __version__ as UEVM_version
from UEVaultManager.api.egs import EPCAPI, GrabResult
from UEVaultManager.api.uevm import UEVMAPI
from UEVaultManager.downloader.mp.DLManagerClass import DLManager
from UEVaultManager.lfs.EPCLFSClass import EPCLFS
from UEVaultManager.lfs.UEVMLFSClass import UEVMLFS
from UEVaultManager.lfs.utils import clean_filename, path_join
from UEVaultManager.models.Asset import Asset, AssetBase, InstalledAsset
from UEVaultManager.models.downloading import AnalysisResult, ConditionCheckResult
from UEVaultManager.models.exceptions import InvalidCredentialsError
from UEVaultManager.models.json_manifest import JSONManifest
from UEVaultManager.models.manifest import Manifest
from UEVaultManager.tkgui.modules.functions import box_message
from UEVaultManager.tkgui.modules.functions_no_deps import format_size
from UEVaultManager.utils.cli import check_and_create_file, check_and_create_folder, get_max_threads
from UEVaultManager.utils.egl_crypt import decrypt_epic_data
from UEVaultManager.utils.env import is_windows_mac_or_pyi

# make some properties of the AppCore class accessible from outside to limit the number of imports needed
default_datetime_format: str = '%Y-%m-%d %H:%M:%S'


class AppCore:
    """
    AppCore handles most of the lower level interaction with
    the downloader, lfs, and api components to make writing CLI/GUI
    code easier and cleaner and avoid duplication.
    :param override_config: path to a config file to use instead of the default.
    :param timeout: timeout for the request. Could be a float or a tuple of float (connect timeout, read timeout).
    """
    _egl_version = '11.0.1-14907503+++Portal+Release-Live'

    def __init__(self, override_config=None, timeout=(7, 7)):
        self.timeout = timeout
        self.log = logging.getLogger('Core')
        self.egs = EPCAPI(timeout=self.timeout)
        self.uevmlfs = UEVMLFS(config_file=override_config)
        self.egl = EPCLFS()
        self.uevm_api = UEVMAPI()

        # on non-Windows load the programdata path from config
        if os.name != 'nt':
            self.egl.programdata_path = self.uevmlfs.config.get('UEVaultManager', 'egl_programdata', fallback=None)
            if self.egl.programdata_path and not os.path.exists(self.egl.programdata_path):
                self.log.error(f'Config EGL path ("{self.egl.programdata_path}") is invalid! Disabling sync...')
                self.egl.programdata_path = None
                self.uevmlfs.config.remove_option('UEVaultManager', 'egl_programdata')
                self.uevmlfs.save_config()

        self.local_timezone = datetime.now().astimezone().tzinfo
        self.language_code, self.country_code = ('en', 'US')

        if locale := self.uevmlfs.config.get('UEVaultManager', 'locale', fallback=getlocale(LC_CTYPE)[0]):
            try:
                self.language_code, self.country_code = locale.split('-' if '-' in locale else '_')
                self.log.debug(f'Set locale to {self.language_code}-{self.country_code}')
                # adjust egs api language as well
                self.egs.language_code, self.egs.country_code = self.language_code, self.country_code
            except Exception as error:
                self.log.warning(f'Getting locale failed: {error!r}, falling back to using en-US.')
        elif system() != 'Darwin':  # macOS doesn't have a default locale we can query
            self.log.warning('Could not determine locale, falling back to en-US')

        self.update_available = False
        self.force_show_update = False
        self.webview_killswitch = False
        self.logged_in = False

        # UE assets metadata cache properties
        self.ue_assets_count = 0
        self.cache_is_invalidate = False
        # Delay (in seconds) when UE assets metadata cache will be invalidated. Default value is 15 days
        self.ue_assets_max_cache_duration = 15 * 24 * 3600
        # set to True to add print more information during long operations
        self.verbose_mode = False
        # Create a backup of the output file (when using the --output option) suffixed by a timestamp before creating a new file
        self.create_output_backup = True
        # Set the file name (and path) to log issues when an asset is ignored or filtered when running the --list command
        self.ignored_assets_filename_log = ''
        # Set the file name (and path) to log issues when an asset is not found on the marketplace when running the --list command
        self.notfound_assets_filename_log = ''
        # Set the file name (and path) to log issues when an asset has metadata and extra data are incoherent when running the --list command
        self.bad_data_assets_filename_log = ''
        # Set the file name (and path) to log issues when scanning folder to find assets
        self.scan_assets_filename_log = ''
        # Create a backup of the log files that store asset analysis suffixed by a timestamp before creating a new file
        self.create_log_backup = True
        # new file loggers
        self.ignored_logger = None
        self.notfound_logger = None
        self.bad_data_logger = None
        self.scan_assets_logger = None
        # store time to process metadata and extra update
        self.process_time_average = {'time': 0.0, 'count': 0}
        self.use_threads = False
        self.thread_executor = None
        self.thread_executor_must_stop = False
        self.engine_version_for_obsolete_assets = gui_g.s.engine_version_for_obsolete_assets

    @staticmethod
    def load_manifest(data: bytes) -> Manifest:
        """
        Load a manifest.
        :param data: bytes object to load the manifest from.
        :return: manifest object.
        """
        if data[0:1] == b'{':
            return JSONManifest.read_all(data)
        else:
            return Manifest.read_all(data)

    @staticmethod
    def check_installation_conditions(analysis: AnalysisResult, folders: [], ignore_space_req: bool = False) -> ConditionCheckResult:
        """
        Check installation conditions.
        :param analysis: analysis result to check.
        :param folders: folders to check free size for.
        :param ignore_space_req:
        :return:
        """
        results = ConditionCheckResult(failures=set(), warnings=set())
        if not isinstance(folders, list):
            folders = [folders]
        for folder in folders:
            if not folder:
                results.failures.add(f'"At least one folder is not defined. Check your config and command options.')
                break
            if not os.path.exists(folder):
                results.failures.add(
                    f'"{folder}" does not exist. Check your config and command options and make sure all necessary disks are available.'
                )
                break
            min_disk_space = analysis.disk_space_delta
            _, _, free = shutil.disk_usage(folder)
            if free < min_disk_space:
                free_gib = free / 1024 ** 3
                required_gib = min_disk_space / 1024 ** 3
                message = f'"{folder}": Potentially not enough available disk space: {free_gib:.02f} GiB < {required_gib:.02f} GiB'
                if ignore_space_req:
                    results.warnings.add(message)
                else:
                    results.failures.add(message)
        return results

    def log_info_and_gui_display(self, message: str) -> None:
        """
        Wrapper to log a message using a log function AND use a DisplayWindows to display the message if the gui is active.
        :param message: message to log.
        """
        self.log.info(message)
        if gui_g.display_content_window_ref is not None:
            gui_g.display_content_window_ref.display(message)

    def setup_assets_loggers(self) -> None:
        """
        Setup logging for ignored, not found and bad data assets.
        """

        def create_logger(logger_name: str, filename_log: str):
            """
            Create a logger for ignored, not found and bad data assets.
            :param logger_name: logger name.
            :param filename_log: log file name.
            :return: logger.
            """
            filename_log = filename_log.replace('~/.config', self.uevmlfs.path)
            if check_and_create_file(filename_log):
                handler = logging.FileHandler(filename_log, mode='w')
                handler.setFormatter(formatter)
                logger = logging.Logger(logger_name, 'INFO')
                logger.addHandler(handler)
                logger.info(message)
                return logger
            else:
                self.log.warning(f'Failed to create logger for file: {filename_log}')
                return None

        formatter = logging.Formatter('%(message)s')
        message = f"-----\n{datetime.now().strftime(default_datetime_format)} Log Started\n-----\n"

        if self.ignored_assets_filename_log:
            self.ignored_logger = create_logger('IgnoredAssets', self.ignored_assets_filename_log)
        if self.notfound_assets_filename_log:
            self.notfound_logger = create_logger('NotFoundAssets', self.notfound_assets_filename_log)
        if self.bad_data_assets_filename_log:
            self.bad_data_logger = create_logger('BadDataAssets', self.bad_data_assets_filename_log)
        if self.scan_assets_filename_log:
            self.scan_assets_logger = create_logger('ScanAssets', self.scan_assets_filename_log)

    def auth_sid(self, sid) -> str:
        """
        Handles getting an exchange code from an id.
        :param sid: session id.
        :return: exchange code.
        """
        s = session()
        s.headers.update(
            {
                'X-Epic-Event-Action':
                'login',
                'X-Epic-Event-Category':
                'login',
                'X-Epic-Strategy-Flags':
                '',
                'X-Requested-With':
                'XMLHttpRequest',
                'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                f'EpicGamesLauncher/{self._egl_version} '
                'UnrealEngine/4.23.0-14907503+++Portal+Release-Live '
                'Chrome/84.0.4147.38 Safari/537.36'
            }
        )
        s.cookies['EPIC_COUNTRY'] = self.country_code.upper()

        # get first set of cookies (EPIC_BEARER_TOKEN etc.)
        _ = s.get('https://www.epicgames.com/id/api/set-sid', params=dict(sid=sid))
        # get XSRF-TOKEN and EPIC_SESSION_AP cookie
        _ = s.get('https://www.epicgames.com/id/api/csrf')
        # finally, get the exchange code
        r = s.post('https://www.epicgames.com/id/api/exchange/generate', headers={'X-XSRF-TOKEN': s.cookies['XSRF-TOKEN']})

        if r.status_code == 200:
            return r.json()['code']

        self.log.error(f'Getting exchange code failed: {r.json()}')
        return ''

    def auth_code(self, code) -> bool:
        """
        Handles authentication via authorization code (either retrieved manually or automatically).
        """
        try:
            self.uevmlfs.userdata = self.egs.start_session(authorization_code=code)
            return True
        except Exception as error:
            self.log.error(f'Log in failed with {error!r}, please try again.')
            return False

    def auth_ex_token(self, code) -> bool:
        """
        Handles authentication via exchange token (either retrieved manually or automatically).
        """
        try:
            self.uevmlfs.userdata = self.egs.start_session(exchange_token=code)
            return True
        except Exception as error:
            self.log.error(f'Log in failed with {error!r}, please try again.')
            return False

    def auth_import(self) -> bool:
        """
        Import refresh token from EGL installation and use it to log in.
        :return: True if successful, False otherwise.
        """
        remember_me_data = self.egl.config.get('RememberMe', 'Data')
        raw_data = b64decode(remember_me_data)
        # data is encrypted
        if raw_data[0] != '{':
            for data_key in self.egl.data_keys:
                try:
                    decrypted_data = decrypt_epic_data(data_key, raw_data)
                    re_data = json.loads(decrypted_data)[0]
                    break
                except Exception as error:
                    self.log.debug(f'Decryption with key {data_key} failed with {error!r}')
            else:
                raise ValueError('Decryption of EPIC launcher user information failed.')
        else:
            re_data = json.loads(raw_data)[0]

        if 'Token' not in re_data:
            raise ValueError('No login session in config')
        refresh_token = re_data['Token']
        try:
            self.uevmlfs.userdata = self.egs.start_session(refresh_token=refresh_token)
            return True
        except Exception as error:
            self.log.error(f'Logging failed with {error!r}, please try again.')
            return False

    def login(self, force_refresh: bool = False, raise_error: bool = True) -> bool:
        """
        Attempt log in with existing credentials.
        :param force_refresh: whether to force a refresh of the session.
        :param raise_error: whether to raise an exception if login fails.
        :return: True if successful, False otherwise.
        """
        if not self.uevmlfs.userdata:
            if raise_error:
                raise ValueError('No saved credentials')
            else:
                self.logged_in = False
                return False
        elif self.logged_in and self.uevmlfs.userdata['expires_at']:
            dt_exp = datetime.fromisoformat(self.uevmlfs.userdata['expires_at'][:-1])
            dt_now = datetime.utcnow()
            td = dt_now - dt_exp

            # if session still has at least 10 minutes left we can re-use it.
            if dt_exp > dt_now and abs(td.total_seconds()) > 600:
                return True
            else:
                self.logged_in = False

        # run update check
        if self.update_check_enabled():
            try:
                self.check_for_updates()
            except Exception as error:
                self.log.warning(f'Checking for UEVaultManager updates failed: {error!r}')

        if self.uevmlfs.userdata['expires_at'] and not force_refresh:
            dt_exp = datetime.fromisoformat(self.uevmlfs.userdata['expires_at'][:-1])
            dt_now = datetime.utcnow()
            td = dt_now - dt_exp

            # if session still has at least 10 minutes left we can re-use it.
            if dt_exp > dt_now and abs(td.total_seconds()) > 600:
                self.log.info('Trying to re-use existing login session...')
                try:
                    self.egs.resume_session(self.uevmlfs.userdata)
                    self.logged_in = True
                    return True
                except InvalidCredentialsError as error:
                    self.log.warning(f'Resuming failed due to invalid credentials: {error!r}')
                except Exception as error:
                    self.log.warning(f'Resuming failed for unknown reason: {error!r}')
                # If verify fails just continue the normal authentication process
                self.log.info('Falling back to using refresh token...')

        try:
            self.log.info('Logging in...')
            userdata = self.egs.start_session(self.uevmlfs.userdata['refresh_token'])
        except InvalidCredentialsError:
            self.log.error('Stored credentials are no longer valid! Please log in again.')
            self.uevmlfs.invalidate_userdata()
            return False
        except (HTTPError, ConnectionError) as error:
            self.log.error(f'HTTP request for log in failed: {error!r}, please try again later.')
            return False

        self.uevmlfs.userdata = userdata
        self.logged_in = True
        return True

    def update_check_enabled(self) -> bool:
        """
        Return whether update checks are enabled or not.
        :return: True if update checks are enabled, False otherwise.
        """
        return not self.uevmlfs.config.getboolean('UEVaultManager', 'disable_update_check', fallback=False)

    def update_notice_enabled(self) -> bool:
        """
        Return whether update notices are enabled or not.
        :return: True if update notices are enabled, False otherwise.
        """
        if self.force_show_update:
            return True
        return not self.uevmlfs.config.getboolean('UEVaultManager', 'disable_update_notice', fallback=not is_windows_mac_or_pyi())

    def check_for_updates(self, force=False) -> None:
        """
        Check for updates and sets the update_available flag accordingly.
        :param force: force update check.
        """

        def version_tuple(v):
            """
            Convert a version string to a tuple of ints.
            :param v: version string.
            :return:  tuple of ints.
            """
            return tuple(map(int, (v.split('.'))))

        cached = self.uevmlfs.get_online_version_saved()
        version_info = cached['data']
        if force or not version_info or (datetime.now().timestamp() - cached['last_update']) > 24 * 3600:
            version_info = self.uevm_api.get_online_version_information()
            self.uevmlfs.set_online_version_saved(version_info)

        web_version = version_info['version']
        self.update_available = version_tuple(web_version) > version_tuple(UEVM_version)

    def get_update_info(self) -> dict:
        """
        Return update info dict.
        :return: update info dict.
        """
        return self.uevmlfs.get_online_version_saved()['data']

    def get_assets(self, update_assets=False, platform='Windows') -> List[AssetBase]:
        """
        Return a list of assets for the given platform.
        :param update_assets: whether to always fetches a new list of assets from the server.
        :param platform: platform to fetch assets for.
        :return: list of AssetBase objects.
        """
        # do not save and always fetch list when platform is overridden
        if not self.uevmlfs.assets or update_assets or platform not in self.uevmlfs.assets:
            # if not logged in, return empty list
            if not self.egs.user:
                return []

            assets = self.uevmlfs.assets.copy() if self.uevmlfs.assets else {}

            assets.update({platform: [AssetBase.from_egs_json(a) for a in self.egs.get_item_assets(platform=platform)]})

            # only save (and write to disk) if there were changes
            if self.uevmlfs.assets != assets:
                self.uevmlfs.assets = assets

        assets = self.uevmlfs.assets.get(platform, None)
        return assets

    def get_asset(self, app_name: str, platform='Windows', update=False) -> AssetBase:
        """
        Return an AssetBase object for the given asset name and platform.
        :param app_name: asset name to get.
        :param platform: platform to get asset for.
        :param update: force update of asset list.
        :return: appAsset object.
        """
        if update or platform not in self.uevmlfs.assets:
            self.get_assets(update_assets=True, platform=platform)

        try:
            return next(i for i in self.uevmlfs.assets[platform] if i.app_name == app_name)
        except StopIteration:
            raise ValueError

    def asset_available(self, item: Asset, platform='Windows') -> bool:
        """
        Return whether an asset is available for the given item and platform.
        :param item: item to check.
        :param platform:.
        :return: True if asset is available, False otherwise.
        """
        try:
            asset = self.get_asset(item.app_name, platform=platform)
            return asset is not None
        except ValueError:
            return False

    def get_item(self, app_name, update_meta=False, platform='Windows') -> Asset:
        """
        Return an Asset object.
        :param app_name: name to get.
        :param update_meta: force update of metadata.
        :param platform: platform to get asset for.
        :return: Asset object.
        """
        if update_meta:
            self.get_asset_list(True, platform=platform)
        return self.uevmlfs.get_item_meta(app_name)

    def get_asset_list(self,
                       update_assets=True,
                       platform='Windows',
                       filter_category='',
                       force_refresh=False) -> (List[Asset], Dict[str, List[Asset]]):
        """
        Returns a list of all available assets for the given platform.
        :param update_assets: force update of asset list.
        :param platform: platform to get assets for.
        :param filter_category: filter by category.
        :param force_refresh: force refresh of asset list.
        :return: assets list.
        """

        # Cancel all outstanding tasks and shut down the executor
        def stop_executor(tasks) -> None:
            """
            Cancel all outstanding tasks and shut down the executor.
            :param tasks: tasks to cancel.
            """
            for _, task in tasks.items():
                task.cancel()
            self.thread_executor.shutdown(wait=False)

        def fetch_asset_meta(name: str) -> bool:
            """
            Fetch metadata for the given asset.
            :param name: asset name.
            :return: True if metadata was fetched, False otherwise.
            """
            if (name in currently_fetching or not fetch_list.get(name)) and ('Asset_Fetcher' in thread_enumerate()) or self.thread_executor_must_stop:
                return False

            if gui_g.progress_window_ref is not None and not gui_g.progress_window_ref.continue_execution:
                return False

            thread_data = ''
            if self.use_threads:
                thread = current_thread()
                thread_data = f' ==> By Thread name={thread.name}'

            self.log.debug(f'--- START fetching data {name}{thread_data}')

            currently_fetching[name] = True
            start_time = datetime.now()
            name, namespace, catalog_item_id, _process_meta, _process_extra = fetch_list[name]

            if _process_meta:
                try:
                    eg_meta, status_code = self.egs.get_item_info(namespace, catalog_item_id)
                except HTTPError as error_l:
                    self.log.warning(f'Failed to fetch metadata for {name}: {error_l!r}')
                    return False
                if status_code != 200:
                    self.log.warning(f'Failed to fetch metadata for {name}: reponse code = {status_code}')
                    return False

                asset = Asset(app_name=name, app_title=eg_meta['title'], metadata=eg_meta, asset_infos=assets[name])
                self.uevmlfs.set_item_meta(asset.app_name, asset)
                assets[name] = asset

            if _process_extra:
                # we use title because it's less ambiguous than a name when searching an asset
                installed_asset = self.uevmlfs.get_installed_asset(name)
                eg_extra = self.egs.grab_assets_extra(
                    asset_name=name, asset_title=assets[name].app_title, verbose_mode=self.verbose_mode, installed_asset=installed_asset,
                )

                # check for data consistency
                if 'stomt' in app_name.lower() or 'terrainmagic' in app_name.lower():
                    if eg_extra.get('grab_result', '') != GrabResult.NO_ERROR.name or not eg_extra.get('owned', False):
                        box_message(
                            msg=f'Some results in extra data are inconsistants for {app_name}. Please check the data and try again. Exiting...',
                            level='error'
                        )

                self.uevmlfs.set_item_extra(app_name=name, extra=eg_extra, update_global_dict=True)

                # log the asset if the title in metadata and the title in the marketplace grabbed page are not identical
                if eg_extra['page_title'] != '' and eg_extra['page_title'] != assets[name].app_title:
                    self.log.warning(f'{name} has incoherent data. It has been added to the bad_data_logger file')
                    eg_extra['grab_result'] = GrabResult.INCONSISTANT_DATA.name
                    if self.bad_data_logger:
                        self.bad_data_logger.info(name)
            else:
                # if we don't process extra, we still need to add the asset to the log corresponding to their grab_result
                eg_extra = self.uevmlfs.assets_extra_data[app_name]
                if eg_extra['grab_result'] == GrabResult.INCONSISTANT_DATA.name and self.bad_data_logger:
                    self.bad_data_logger.info(name)
                if eg_extra['grab_result'] == GrabResult.CONTENT_NOT_FOUND.name and self.notfound_logger:
                    self.notfound_logger.info(name)
            # compute process time and average in s
            end_time = datetime.now()
            process_time = (end_time - start_time).total_seconds()
            self.process_time_average['time'] += process_time
            self.process_time_average['count'] += 1

            if fetch_list.get(name):
                del fetch_list[name]
                if self.verbose_mode:
                    self.log.info(f'Removed {name} from the metadata update')

            if currently_fetching.get(name):
                del currently_fetching[name]

            if not self.use_threads:
                process_average = self.process_time_average['time'] / self.process_time_average['count']
                self.log.info(f'===Time Average={process_average:.3f} s # ({(len(fetch_list) * process_average):.3f} s time left)')

            self.log.info(
                f'--- END fetching data in {name}{thread_data}. Time For Processing={process_time:.3f}s # Still {len(fetch_list)} assets to process'
            )
            return True

        # end of fetch_asset_meta

        _ret = []
        meta_updated = False

        # fetch asset information for Windows, all installed platforms, and the specified one
        platforms = {'Windows'}
        platforms |= {platform}
        if gui_g.progress_window_ref is not None:
            gui_g.progress_window_ref.reset(new_value=0, new_text="Fetching platforms...", new_max_value=len(platforms))
        for _platform in platforms:
            self.get_assets(update_assets=update_assets, platform=_platform)
            if gui_g.progress_window_ref is not None and not gui_g.progress_window_ref.update_and_continue(increment=1):
                return []

        if not self.uevmlfs.assets:
            return _ret

        assets = {}
        if gui_g.progress_window_ref is not None:
            gui_g.progress_window_ref.reset(new_value=0, new_text="Fetching assets...", new_max_value=len(self.uevmlfs.assets.items()))
        for _platform, _assets in self.uevmlfs.assets.items():
            for _asset in _assets:
                if gui_g.progress_window_ref is not None and not gui_g.progress_window_ref.update_and_continue(increment=1):
                    return []
                if _asset.app_name in assets:
                    assets[_asset.app_name][_platform] = _asset
                else:
                    assets[_asset.app_name] = {_platform: _asset}

        fetch_list = {}
        assets_bypassed = {}
        assets = {}

        # loop through assets items to check for if they are for ue or not
        valid_items = []
        bypass_count = 0
        self.log.info(f'======\nSTARTING phase 1: asset indexing (ue or not)\n')
        if gui_g.progress_window_ref is not None:
            gui_g.progress_window_ref.reset(new_value=0, new_text="Indexing assets...", new_max_value=len(assets.items()))
        # Note: we sort by reverse, as it the most recent version of an asset will be listed first
        for app_name, app_assets in sorted(assets.items(), reverse=True):
            if gui_g.progress_window_ref is not None and not gui_g.progress_window_ref.update_and_continue(increment=1):
                return []
            # Note:
            #   asset_id is not unique because somme assets can have the same asset_id but with several UE versions
            #   app_name is unique because it includes the unreal version
            # asset_id = app_assets['Windows'].asset_id
            assets_bypassed[app_name] = False
            if app_assets['Windows'].namespace != 'ue':
                self.log.debug(f'{app_name} has been bypassed (namespace != "ue") in phase 1')
                bypass_count += 1
                assets_bypassed[app_name] = True
                continue

            item = {'name': app_name, 'asset': app_assets}
            valid_items.append(item)

        self.ue_assets_count = len(valid_items)

        self.log.info(f'A total of {bypass_count} on {len(valid_items)} assets have been bypassed in phase 1')

        # check if we must refresh ue asset metadata cache
        self.check_for_ue_assets_updates(self.ue_assets_count, force_refresh)
        force_refresh = self.cache_is_invalidate
        if force_refresh:
            self.log.info(f'!! Assets metadata will be updated !!\n')
        else:
            self.log.info(f"Asset metadata won't be updated\n")

        self.log.info(f'======\nSTARTING phase 2:asset filtering and metadata updating\n')
        if gui_g.progress_window_ref is not None:
            gui_g.progress_window_ref.reset(new_value=0, new_text="Updating metadata...", new_max_value=len(valid_items))
        # loop through valid items to check for update and filtering
        bypass_count = 0
        filtered_items = []
        currently_fetching = {}
        i = 0
        while i < len(valid_items):
            if gui_g.progress_window_ref is not None and not gui_g.progress_window_ref.update_and_continue(increment=1):
                return []
            item = valid_items[i]
            app_name = item['name']
            app_assets = item['asset']
            if self.verbose_mode:
                self.log.info(f'Checking {app_name}....')

            item_metadata = self.uevmlfs.get_item_meta(app_name)
            asset_updated = False

            if not item_metadata:
                self.log.info(f'Metadata for {app_name} are missing. It Will be ADDED to the FETCH list')
            else:
                category_lower = str(item_metadata.metadata['categories'][0]['path']).lower()
                if filter_category and filter_category.lower() not in category_lower:
                    self.log.info(
                        f'{app_name} has been FILTERED by category ("{filter_category}" text not found in "{category_lower}").It has been added to the ignored_logger file'
                    )
                    if self.ignored_logger:
                        self.ignored_logger.info(app_name)
                    assets_bypassed[app_name] = True
                    bypass_count += 1
                    i += 1
                    continue
                asset_updated = any(item_metadata.app_version(_p) != app_assets[_p].build_version for _p in app_assets.keys())
                assets[app_name] = item_metadata
                self.log.debug(f'{app_name} has been ADDED to the assets list with asset_updated={asset_updated}')

            # get extra data only in not filtered
            if force_refresh or asset_updated:
                process_extra = True
            else:
                # will read the extra data from file if necessary and put in the global dict
                process_extra = self.uevmlfs.get_item_extra(app_name) is None

            process_meta = not item_metadata or force_refresh or asset_updated

            if update_assets and (process_extra or process_meta):
                self.log.debug(f'Scheduling metadata and extra update for {app_name}')
                # namespace/catalog item are the same for all platforms, so we can just use the first one
                _ga = next(iter(app_assets.values()))
                fetch_list[app_name] = (app_name, _ga.namespace, _ga.catalog_item_id, process_meta, process_extra)
                meta_updated = True
            i += 1
            filtered_items.append(item)
        # end while i < len(valid_items):

        # setup and teardown of thread pool takes some time, so only do it when it makes sense.
        self.use_threads = len(fetch_list) > 5
        # self.use_threads = False  # Debug only
        if fetch_list:
            if gui_g.progress_window_ref is not None:
                gui_g.progress_window_ref.reset(
                    new_value=0, new_text="Fetching missing metadata...\nIt could take some time. Be patient.", new_max_value=len(fetch_list)
                )
                # gui_g.progress_window_ref.hide_progress_bar()
                # gui_g.progress_window_ref.hide_btn_stop()

            self.log.info(f'Fetching metadata for {len(fetch_list)} asset(s).')
            if self.use_threads:
                # Note:  unreal engine API limits the number of connection to 16. So no more than 15 threads to avoid connection refused

                # with ThreadPoolExecutor(max_workers=min(16, os.cpu_count() - 2), thread_name_prefix="Asset_Fetcher") as executor:
                #    executor.map(fetch_asset_meta, fetch_list.keys(), timeout=30.0)
                self.thread_executor = ThreadPoolExecutor(max_workers=get_max_threads(), thread_name_prefix="Asset_Fetcher")
                # Dictionary that maps each key to its corresponding Future object
                futures = {}
                for key in fetch_list.keys():
                    # Submit the task and add its Future to the dictionary
                    future = self.thread_executor.submit(fetch_asset_meta, key)
                    futures[key] = future

                with concurrent.futures.ThreadPoolExecutor():
                    for future in concurrent.futures.as_completed(futures.values()):
                        try:
                            _ = future.result()
                            # print("Result: ", result)
                        except Exception as error:
                            self.log.warning(f'The following error occurs in threading: {error!r}')
                        if gui_g.progress_window_ref is not None and not gui_g.progress_window_ref.continue_execution:
                            # self.log.info(f'User stop has been pressed. Stopping running threads....')  # will flood console
                            stop_executor(futures)
                self.thread_executor.shutdown(wait=False)

        self.log.info(f'A total of {bypass_count} on {len(valid_items)} assets have been bypassed in phase 2')
        self.log.info(f'======\nSTARTING phase 3: emptying the List of assets to be fetched \n')
        if gui_g.progress_window_ref is not None:
            # gui_g.progress_window_ref.show_progress_bar()  # show progress bar, must be before reset
            gui_g.progress_window_ref.show_btn_stop()
            gui_g.progress_window_ref.reset(new_value=0, new_text="Checking and Fetching asset's data...", new_max_value=len(filtered_items))
        # loop through valid and filtered items
        meta_updated = (bypass_count == 0) and meta_updated  # to avoid deleting metadata files or assets that have been filtered
        fetch_try_count = {}
        fetch_try_limit = 3
        while len(filtered_items) > 0:
            if gui_g.progress_window_ref is not None and not gui_g.progress_window_ref.update_and_continue(increment=1):
                return []
            item = filtered_items.pop()
            app_name = item['name']
            app_assets = item['asset']
            if fetch_try_count.get(app_name):
                fetch_try_count[app_name] += 1
            else:
                fetch_try_count[app_name] = 1
            if self.verbose_mode:
                self.log.info(f'Checking {app_name} Try number = {fetch_try_count[app_name]}. Still {len(filtered_items)} assets to check')
            try:
                app_item = assets.get(app_name)
            except (KeyError, IndexError):
                self.log.debug(f'{app_name} has not been found int the asset list. Bypassing')
                # item not found in asset, ignore and pass to next one
                continue
            # retry if the asset is still in fetch list (with active fetcher treads)
            if fetch_list.get(app_name) and (not currently_fetching.get(app_name) or 'Asset_Fetcher' not in thread_enumerate()):
                self.log.info(f'Fetching metadata for {app_name} is still no done, retrying')
                if currently_fetching.get(app_name):
                    del currently_fetching[app_name]
                fetch_asset_meta(app_name)

            if fetch_try_count[app_name] > fetch_try_limit:
                self.log.error(f'Fetching metadata for {app_name} has failed {fetch_try_limit} times. Skipping')
                continue
            try:
                is_bypassed = (app_name in assets_bypassed) and (assets_bypassed[app_name])
                is_a_mod = any(i['path'] == 'mods' for i in app_item.metadata.get('categories', []))
            except (KeyError, IndexError, AttributeError):
                self.log.debug(f'{app_name} has no metadata. Adding to the fetch list (again)')
                try:
                    fetch_list[app_name] = (app_name, item.namespace, item.catalog_item_id, True, True)
                    _ret.append(app_item)
                except (KeyError, IndexError, AttributeError):
                    self.log.debug(f'{app_name} has an invalid format. Could not been added to the fetch list')
                continue

            has_valid_platform = platform in app_assets
            is_still_fetching = (app_name in fetch_list) or (app_name in currently_fetching)

            if is_still_fetching:
                # put again the asset in the list waiting when it will be fetched
                filtered_items.append(item)
                time.sleep(3)  # Sleep for 3 seconds to let the fetch process progress or end

            # check if the asset will be added to the final list
            if not is_bypassed and not is_still_fetching and not is_a_mod and has_valid_platform:
                _ret.append(app_item)

        self.log.info(f'A total of {len(_ret)} assets have been analysed and kept in phase 3')

        if gui_g.s.never_update_data_files:
            meta_updated = False
        if meta_updated:
            if gui_g.progress_window_ref is not None:
                gui_g.progress_window_ref.reset(new_value=0, new_text="Updating metadata files...", new_max_value=len(_ret))
            self.log.info(f'Updating metadata files...Could take a some time')
            self._prune_metadata()
            self._save_metadata(_ret)
        if meta_updated:
            if gui_g.progress_window_ref is not None:
                gui_g.progress_window_ref.reset(new_value=0, new_text="Updating extra data files...", new_max_value=len(_ret))
            self.log.info(f'Updating extra data files...Could take a some time')
            self._prune_extra_data(update_global_dict=False)
            self._save_extra_data(self.uevmlfs.assets_extra_data, update_global_dict=False)
        return _ret

    # end def get_asset_list(self, update_assets=True, platform='Windows', filter_category='') -> (List[asset], Dict[str, List[asset]]):

    def _prune_metadata(self) -> None:
        """
        Compile a list of assets without assets, then delete their metadata.
        """
        # compile list of assets without assets, then delete their metadata
        owned_assets = set()
        owned_assets |= {i.app_name for i in self.get_assets(platform='Windows')}

        for app_name in self.uevmlfs.get_item_app_names():
            self.log.debug(f'Removing old/unused metadata for "{app_name}"')
            self.uevmlfs.delete_item_meta(app_name)

    def _prune_extra_data(self, update_global_dict: True) -> None:
        """
        Compile a list of assets without assets, then delete their extra data.
        :param update_global_dict:  if True, update the global dict.
        """
        owned_assets = set()
        owned_assets |= {i.app_name for i in self.get_assets(platform='Windows')}

        for app_name in self.uevmlfs.get_item_app_names():
            self.log.debug(f'Removing old/unused extra data for "{app_name}"')
            self.uevmlfs.delete_item_extra(app_name, update_global_dict=update_global_dict)

    def _save_metadata(self, assets) -> None:
        """
        Save the metadata for the given assets.
        :param assets:  List of assets to save.
        """
        self.log.info('Saving metadata in files... could take some time')
        for asset in assets:
            if gui_g.progress_window_ref is not None and not gui_g.progress_window_ref.update_and_continue(increment=1):
                return
            self.uevmlfs.set_item_meta(asset.app_name, asset)

    def _save_extra_data(self, extra: dict, update_global_dict: True) -> None:
        """
        Save the extra data for the given assets.
        :param extra: dict of extra data to save.
        :param update_global_dict: whether to update the global dict.
        """
        self.log.info('Saving extra data in files... could take some time')
        for app_name, eg_extra in extra.items():
            if gui_g.progress_window_ref is not None and not gui_g.progress_window_ref.update_and_continue(increment=1):
                return
            self.uevmlfs.set_item_extra(app_name=app_name, extra=eg_extra, update_global_dict=update_global_dict)

    def is_installed(self, app_name: str) -> bool:
        """
        Return whether an asset is installed.
        :param app_name: asset name to check.
        :return: True if asset is installed, False otherwise.
        """
        return self.uevmlfs.get_installed_asset(app_name) is not None

    def get_non_asset_library_items(self, force_refresh=False, skip_ue=True) -> (List[Asset], Dict[str, List[Asset]]):
        """
        Gets a list of Items without assets for installation, for instance Items delivered via
        third-party stores that do not have assets for installation.
        :param force_refresh: force a metadata refresh.
        :param skip_ue: ignore Unreal Marketplace entries.
        :return: list of Items that do not have assets.
        """
        _ret = []
        # get all the asset names we have to ignore
        ignore = set(i.app_name for i in self.get_assets())

        for lib_item in self.egs.get_library_items():
            if lib_item['namespace'] == 'ue' and skip_ue:
                continue
            if lib_item['appName'] in ignore:
                continue

            item = self.uevmlfs.get_item_meta(lib_item['appName'])
            if not item or force_refresh:
                eg_meta, status_code = self.egs.get_item_info(lib_item['namespace'], lib_item['catalogItemId'])
                if status_code != 200:
                    self.log.warning(f'Failed to fetch metadata for {lib_item["appName"]}: reponse code = {status_code}')
                    continue
                item = Asset(app_name=lib_item['appName'], app_title=eg_meta['title'], metadata=eg_meta)
                self.uevmlfs.set_item_meta(item.app_name, item)

            if not any(i['path'] == 'mods' for i in item.metadata.get('categories', [])):
                _ret.append(item)

        return _ret

    def get_installed_manifest(self, app_name):
        """
        Get the installed manifest.
        :param app_name: asset name to get the installed manifest for.
        :return:
        """
        installed_asset = self.uevmlfs.get_installed_asset(app_name)
        old_bytes = self.uevmlfs.load_manifest(app_name, installed_asset.version, installed_asset.platform)
        return old_bytes, installed_asset.base_urls

    def get_cdn_urls(self, item, platform='Windows'):
        """
        Get the CDN URLs.
        :param item: item to get the CDN URLs for.
        :param platform: platform to get the CDN URLs for.
        :return: list of CDN URLs.
        """
        m_api_r = self.egs.get_item_manifest(item.namespace, item.catalog_item_id, item.app_name, platform)

        # never seen this outside the launcher itself, but if it happens: PANIC!
        if len(m_api_r['elements']) > 1:
            raise ValueError('Manifest response has more than one element!')

        manifest_hash = m_api_r['elements'][0]['hash']
        base_urls = []
        manifest_urls = []
        for manifest in m_api_r['elements'][0]['manifests']:
            base_url = manifest['uri'].rpartition('/')[0]
            if base_url not in base_urls:
                base_urls.append(base_url)

            if 'queryParams' in manifest:
                params = '&'.join(f'{p["name"]}={p["value"]}' for p in manifest['queryParams'])
                manifest_urls.append(f'{manifest["uri"]}?{params}')
            else:
                manifest_urls.append(manifest['uri'])

        return manifest_urls, base_urls, manifest_hash

    def get_cdn_manifest(self, item, platform='Windows', disable_https=False):
        """
        Get the CDN manifest.
        :param item: item to get the CDN manifest for.
        :param platform: platform to get the CDN manifest for.
        :param disable_https: disable HTTPS for the manifest URLs.
        :return: tuple (manifest data, base URLs, request status code).
        """
        manifest_urls, base_urls, manifest_hash = self.get_cdn_urls(item, platform)
        if not manifest_urls:
            raise ValueError('No manifest URLs returned by API')

        if disable_https:
            manifest_urls = [url.replace('https://', 'http://') for url in manifest_urls]

        r = {}
        for url in manifest_urls:
            self.log.debug(f'Trying to download manifest from "{url}"...')
            try:
                r = self.egs.unauth_session.get(url, timeout=self.timeout)
            except Exception as error:
                self.log.warning(f'Failed to download manifest from "{urlparse(url).netloc}" (Exception: {error!r}), trying next URL...')
                continue

            if r.status_code == 200:
                manifest_bytes = r.content
                break
            else:
                self.log.warning(f'Failed to download manifest from "{urlparse(url).netloc}" (status: {r.status_code}), trying next URL...')
        else:
            raise ValueError(f'Failed to get manifest from any CDN URL, last result: {r.status_code} ({r.reason})')

        if sha1(manifest_bytes).hexdigest() != manifest_hash:
            raise ValueError('Manifest sha hash mismatch!')

        return manifest_bytes, base_urls, r.status_code

    def get_uri_manifest(self, uri: str) -> (bytes, List[str]):
        """
        Get the manifest.
        :param uri: uRI to get the manifest from.
        :return:  Manifest data and base URLs.
        """
        if uri.startswith('http'):
            r = self.egs.unauth_session.get(uri)
            r.raise_for_status()
            new_manifest_data = r.content
            base_urls = [r.url.rpartition('/')[0]]
        else:
            base_urls = []
            with open(uri, 'rb') as f:
                new_manifest_data = f.read()

        return new_manifest_data, base_urls

    def prepare_download(
        self,
        base_asset: Asset,  # contains generic info of the base asset for all releases, NOT the selected release
        release_name: str,
        release_title: str,
        download_folder: str = '',
        install_folder: str = '',
        no_resume: bool = False,
        platform: str = 'Windows',
        max_shm: int = 0,
        max_workers: int = 0,
        dl_optimizations: bool = False,
        override_manifest: str = '',
        override_old_manifest: str = '',
        override_base_url: str = '',
        status_queue: Queue = None,
        reuse_last_install: bool = False,
        disable_patching: bool = False,
        file_prefix_filter: list = None,
        file_exclude_filter: list = None,
        file_install_tag: list = None,
        preferred_cdn: str = None,
        disable_https: bool = False
    ) -> (DLManager, AnalysisResult, InstalledAsset):
        """
        Prepare a download.
        :param base_asset: the "base" asset to prepare the download for, not the selected release.
        :param release_name: release name prepare the download for.
        :param release_title: release title prepare the download for.
        :param download_folder: folder to download the asset to.
        :param install_folder: base folder to install the asset to.
        :param platform: platform to prepare the download for.
        :param no_resume: avoid to resume. Force a new download.
        :param max_shm: maximum amount of shared memory to use.
        :param max_workers: maximum number of workers to use.
        :param dl_optimizations: download optimizations.
        :param override_manifest: override the manifest.
        :param override_old_manifest: override the old manifest.
        :param override_base_url: override the base URL.
        :param reuse_last_install: update previous installation.
        :param disable_patching: disable patching.
        :param status_queue: status queue to send status updates to.
        :param file_prefix_filter: file prefix filter.
        :param file_exclude_filter: file exclude filter.
        :param file_install_tag: file install tag.
        :param preferred_cdn: preferred CDN.
        :param disable_https: disable HTTPS. For LAN installs only.
        :return: (DLManager object, AnalysisResult object, InstalledAsset object).
        """
        old_manifest = None
        egl_guid = ''

        # load old manifest if we have one
        if override_old_manifest:
            self.log.info(f'Overriding old manifest with "{override_old_manifest}"')
            old_bytes, _ = self.get_uri_manifest(override_old_manifest)
            old_manifest = self.load_manifest(old_bytes)
        elif not disable_patching and not no_resume and self.is_installed(release_name):
            old_bytes, _base_urls = self.get_installed_manifest(release_name)
            if _base_urls and not base_asset.base_urls:
                base_asset.base_urls = _base_urls
            if not old_bytes:
                self.log.error(f'Could not load old manifest, patching will not work!')
            else:
                old_manifest = self.load_manifest(old_bytes)

        base_urls = base_asset.base_urls

        # The EGS client uses plaintext HTTP by default for the purposes of enabling simple DNS based
        # CDN redirection to a (local) cache.
        disable_https = disable_https or self.uevmlfs.config.getboolean('UEVaultManager', 'disable_https', fallback=False)

        if override_manifest:
            self.log_info_and_gui_display(f'Overriding manifest with "{override_manifest}"')
            new_manifest_data, _base_urls = self.get_uri_manifest(override_manifest)
            # if override manifest has a base URL use that instead
            if _base_urls:
                base_urls = _base_urls
        else:
            new_manifest_data, base_urls, status_code = self.get_cdn_manifest(base_asset, platform, disable_https=disable_https)
            # overwrite base urls in metadata with current ones to avoid using old/dead CDNs
            base_asset.base_urls = base_urls
            # save base urls to game metadata
            self.uevmlfs.set_item_meta(release_name, base_asset)

        self.log_info_and_gui_display('Parsing game manifest...')
        manifest = self.load_manifest(new_manifest_data)
        self.log.debug(f'Base urls: {base_urls}')
        # save manifest with version name as well for testing/downgrading/etc.
        manifest_filename = self.uevmlfs.save_manifest(release_name, new_manifest_data, version=manifest.meta.build_version, platform=platform)

        # make sure donwnload folder actually exists (but do not create asset folder)
        if not check_and_create_folder(download_folder):
            self.log_info_and_gui_display(f'"{download_folder}" did not exist, it has been created.')
        if not os.access(download_folder, os.W_OK):
            raise PermissionError(f'No write access to "{download_folder}"')

        # reuse existing installation's directory
        installed_asset = self.uevmlfs.get_installed_asset(release_name)
        if reuse_last_install and installed_asset:
            install_path = installed_asset.install_path
            egl_guid = installed_asset.egl_guid
        else:
            # asset are always installed in the 'Content' sub folder
            # NO we don't want to store "content" in the "install path"
            # install_path = path_join(install_folder, 'Content') if install_folder != '' else ''
            install_path = install_folder

        # check for write access on the installation path or its parent directory if it doesn't exist yet
        if not check_and_create_folder(install_path):
            self.log_info_and_gui_display(f'"{install_path}" did not exist, it has been created.')
        if install_path != '' and not os.access(install_path, os.W_OK):
            raise PermissionError(f'No write access to "{install_path}"')

        self.log_info_and_gui_display(f'Install path: {install_path}')

        if not no_resume:
            filename = clean_filename(f'{release_name}.resume')
            resume_file = path_join(self.uevmlfs.tmp_folder, filename)
        else:
            resume_file = None

        # Use user-specified base URL or preferred CDN first, otherwise fall back to
        # EGS's behaviour of just selecting the first CDN in the list.
        base_url = None
        if override_base_url:
            self.log_info_and_gui_display(f'Overriding base URL with "{override_base_url}"')
            base_url = override_base_url
        elif preferred_cdn or (preferred_cdn := self.uevmlfs.config.get('UEVaultManager', 'preferred_cdn', fallback=None)):
            for url in base_urls:
                if preferred_cdn in url:
                    base_url = url
                    break
            else:
                self.log.warning(f'Preferred CDN "{preferred_cdn}" unavailable, using default selection.')
        # Use first, fail if none known
        if not base_url:
            if not base_urls:
                raise ValueError('No base URLs found, please try again.')
            base_url = base_urls[0]

        if disable_https:
            base_url = base_url.replace('https://', 'http://')

        self.log.debug(f'Using base URL: {base_url}')
        scheme, cdn_host = base_url.split('/')[0:3:2]
        self.log_info_and_gui_display(f'Selected CDN: {cdn_host} ({scheme.strip(":")})')

        if not max_shm:
            max_shm = self.uevmlfs.config.getint('UEVaultManager', 'max_memory', fallback=2048)

        if dl_optimizations:
            self.log_info_and_gui_display('Download order optimizations are enabled.')
            process_opt = True
        else:
            process_opt = False

        if not max_workers:
            max_workers = self.uevmlfs.config.getint('UEVaultManager', 'max_workers', fallback=0)

        download_manager = DLManager(
            download_dir=download_folder,
            base_url=base_url,
            resume_file=resume_file,
            status_q=status_queue,
            max_shared_memory=max_shm * 1024 * 1024,
            max_workers=max_workers,
            timeout=self.timeout,
            trace_func=self.log_info_and_gui_display,
        )
        installed_asset = self.uevmlfs.get_installed_asset(release_name)
        if installed_asset is None:
            # create a new installed asset
            installed_asset = InstalledAsset(app_name=release_name, title=release_title)
        # update the installed asset
        installed_asset.version = manifest.meta.build_version
        installed_asset.base_urls = base_urls
        installed_asset.egl_guid = egl_guid
        installed_asset.manifest_path = override_manifest if override_manifest else manifest_filename
        installed_asset.platform = platform
        installed_asset.catalog_item_id = base_asset.catalog_item_id
        already_installed = install_path and install_path in installed_asset.installed_folders
        analyse_res = download_manager.run_analysis(
            manifest=manifest,
            old_manifest=old_manifest,
            patch=not disable_patching,
            resume=not no_resume,
            file_prefix_filter=file_prefix_filter,
            file_exclude_filter=file_exclude_filter,
            file_install_tag=file_install_tag,
            processing_optimization=process_opt,
            already_installed=already_installed
        )
        if install_path != '':
            # will add install_path to the installed_folders list after checking if it is not already in it
            installed_asset.install_path = install_path
        installed_asset.install_size = analyse_res.install_size
        return download_manager, analyse_res, installed_asset

    # Check if the UE assets metadata cache must be updated
    def check_for_ue_assets_updates(self, assets_count: int, force_refresh=False) -> None:
        """
        Check if the UE assets metadata cache must be updated.
        :param assets_count: assets count from the API.
        :param force_refresh: force the refresh of the cache.
        """
        self.cache_is_invalidate = False
        cached = self.uevmlfs.get_assets_cache_info()
        cached_assets_count = cached['ue_assets_count']

        date_now = datetime.now().timestamp()
        date_diff = date_now - cached['last_update']

        if not cached_assets_count or cached_assets_count != assets_count:
            self.log.info(f'New assets are available. {assets_count} available VS {cached_assets_count} in cache')
            self.uevmlfs.set_assets_cache_info(last_update=cached['last_update'], ue_assets_count=assets_count)

        if force_refresh or date_diff > self.ue_assets_max_cache_duration:
            self.cache_is_invalidate = True
            self.uevmlfs.set_assets_cache_info(last_update=date_now, ue_assets_count=assets_count)
            if not force_refresh:
                self.log.info(f'Data cache is outdated. Cache age is {date_diff:.1f} s OR {str(timedelta(seconds=date_diff))}')
        else:
            self.log.info(f'Data cache is still valid. Cache age is {str(timedelta(seconds=date_diff))}')

    def clean_exit(self, code=0) -> None:
        """
        Do cleanup, config saving, and quit.
        :param code: exit code.
        """
        self.uevmlfs.save_config()
        logging.shutdown()
        sys.exit(code)

    def open_manifest_file(self, file_path: str) -> dict:
        """
        Open a manifest file and return its data.
        :param file_path: path to the manifest file.
        :return: manifest data.
        """
        try:
            with open(file_path, 'rb') as file:
                manifest_data = file.read()
        except FileNotFoundError:
            self.log.warning(f'The file {file_path} does not exist.')
            return {}
        manifest_info = {}
        manifest = self.load_manifest(manifest_data)
        manifest_info['app_name'] = manifest.meta.app_name

        # file and chunk count
        manifest_info['num_files'] = manifest.file_manifest_list.count
        manifest_info['num_chunks'] = manifest.chunk_data_list.count
        # total file size
        total_size = sum(fm.file_size for fm in manifest.file_manifest_list.elements)
        file_size = format_size(total_size)
        manifest_info['file_size'] = file_size
        manifest_info['disk_size'] = total_size
        # total chunk size
        total_size = sum(c.file_size for c in manifest.chunk_data_list.elements)
        chunk_size = format_size(total_size)
        manifest_info['chunk_size'] = chunk_size
        manifest_info['download_size'] = total_size
        return manifest_info
