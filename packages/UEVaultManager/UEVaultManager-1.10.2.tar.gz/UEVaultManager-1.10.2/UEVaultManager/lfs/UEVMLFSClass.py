# coding: utf-8
"""
Implementation for:
- UEVMLFS: Local File System.
"""
import filecmp
import json
import logging
import os
from datetime import datetime
from time import time
from typing import Optional

import UEVaultManager.tkgui.modules.globals as gui_g  # using the shortest variable name for globals for convenience
from UEVaultManager.lfs.utils import clean_filename, generate_label_from_path
from UEVaultManager.lfs.utils import path_join
from UEVaultManager.models.AppConfigClass import AppConfig
from UEVaultManager.models.Asset import Asset, AssetBase, InstalledAsset
from UEVaultManager.tkgui.modules.functions import create_file_backup
from UEVaultManager.tkgui.modules.functions_no_deps import merge_lists_or_strings
from UEVaultManager.utils.cli import check_and_create_file
from UEVaultManager.utils.env import is_windows_mac_or_pyi


class UEVMLFS:
    """
    Class to handle all local filesystem related tasks.
    :param config_file: path to config file to use instead of default.
    """

    def __init__(self, config_file=None):
        self.log = logging.getLogger('UEVMLFS')

        if config_path := os.environ.get('XDG_CONFIG_HOME'):
            self.path = path_join(config_path, 'UEVaultManager')
        else:
            self.path = os.path.expanduser('~/.config/UEVaultManager')
        # EGS user info
        self._user_data = None
        # EGS entitlements
        self._entitlements = None
        # EGS asset data
        self._assets = None
        # EGS metadata
        self.assets_metadata = {}
        # additional infos (price, review...)
        self.assets_extra_data = {}
        # UEVaultManager update check info
        self._update_info = None
        # UE assets metadata cache data
        self._assets_cache_info = None
        # store the dowload size of assets
        self._asset_sizes = None

        # Config with item specific settings (e.g. start parameters, env variables)
        self.config = AppConfig(comment_prefixes='/', allow_no_value=True)

        if config_file:
            # if user specified a valid relative/absolute path use that,
            # otherwise create file in UEVaultManager config directory
            if os.path.exists(config_file):
                self.config_file = os.path.abspath(config_file)
            else:
                self.config_file = path_join(self.path, clean_filename(config_file))
            self.log.info(f'UEVMLFS is using non-default config file "{self.config_file}"')
        else:
            self.config_file = path_join(self.path, 'config.ini')

        # Folders used by the application
        self.manifests_folder: str = path_join(self.path, 'manifests')
        self.metadata_folder: str = path_join(self.path, 'metadata')
        self.tmp_folder: str = path_join(self.path, 'tmp')
        self.extra_folder: str = path_join(self.path, 'extra')
        self.json_files_folder: str = path_join(self.path, 'data')  # folder for json files other than metadata, extra and manifests

        # filename for storing the user data (filled by the 'auth' command).
        self.user_data_filename: str = path_join(self.json_files_folder, 'user_data.json')
        # filename for storing data about the current version of the application
        self.online_version_filename: str = path_join(self.json_files_folder, 'online_version.json')
        # filename for storing cache data for asset's metadata updating
        self.assets_cache_info_filename: str = path_join(self.json_files_folder, 'assets_cache_info.json')
        # filename for storing 'basic' data of assets.
        self.assets_data_filename: str = path_join(self.json_files_folder, 'assets.json')
        # filename for the installed assets list
        self.installed_asset_filename: str = path_join(self.json_files_folder, 'installed_assets.json')
        # filename for storing the size of asset (filled by the 'info' command).
        self.asset_sizes_filename: str = path_join(self.json_files_folder, 'asset_sizes.json')

        # ensure folders exist.
        for f in ['', self.manifests_folder, self.metadata_folder, self.tmp_folder, self.extra_folder, self.json_files_folder]:
            if not os.path.exists(path_join(self.path, f)):
                os.makedirs(path_join(self.path, f))

        # check and create some empty files (to avoid file not found errors in debug)
        check_and_create_file(self.assets_data_filename, create_file=False)  # keep the file content as 'None'
        check_and_create_file(self.asset_sizes_filename, content='{}')
        check_and_create_file(self.installed_asset_filename, content='{}')

        try:
            self.config.read(self.config_file)
        except Exception as error:
            self.log.error(f'Failed to read configuration file, please ensure that file is valid!:Error: {error!r}')
            self.log.warning('Continuing with blank config in safe-mode...')
            self.config.read_only = True

        # make sure "UEVaultManager" section exists
        has_changed = False
        if 'UEVaultManager' not in self.config:
            self.config.add_section('UEVaultManager')
            has_changed = True

        # Add opt-out options with explainers
        if not self.config.has_option('UEVaultManager', 'max_memory'):
            self.config.set('UEVaultManager', '; Set preferred CDN host (e.g. to improve download speed)')
            self.config.set('UEVaultManager', 'max_memory', '2048')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'max_workers'):
            self.config.set(
                'UEVaultManager', '; maximum number of worker processes when downloading (fewer will be slower, use less system resources)'
            )
            self.config.set('UEVaultManager', 'max_workers', '8')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'locale'):
            self.config.set('UEVaultManager', '; locale override, must be in RFC 1766 format (e.g. "en-US")')
            self.config.set('UEVaultManager', 'locale', 'en-US')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'egl_programdata'):
            self.config.set('UEVaultManager', '; path to the "Manifests" folder in the EGL ProgramData directory for non Windows platforms')
            self.config.set('UEVaultManager', 'egl_programdata', 'THIS_MUST_BE_SET_ON_NON_WINDOWS_PLATFORMS')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'preferred_cdn'):
            self.config.set('UEVaultManager', '; maximum shared memory (in MiB) to use for installation')
            self.config.set('UEVaultManager', 'preferred_cdn', 'epicgames-download1.akamaized.net')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'disable_https'):
            self.config.set('UEVaultManager', '; disable HTTPS for downloads (e.g. to use a LanCache)')
            self.config.set('UEVaultManager', 'disable_https', 'false')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'disable_update_check'):
            self.config.set('UEVaultManager', ';Set to True to disable the automatic update check')
            self.config.set('UEVaultManager', 'disable_update_check', 'False')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'disable_update_notice'):
            self.config.set('UEVaultManager', '; Set to True to disable the notice about an available update on exit')
            self.config.set('UEVaultManager', 'disable_update_notice', 'False' if is_windows_mac_or_pyi() else 'True')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'start_in_edit_mode'):
            self.config.set('UEVaultManager', ';Set to True to start the application in Edit mode (since v1.4.4) with the GUI')
            self.config.set('UEVaultManager', 'start_in_edit_mode', 'False')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'create_output_backup'):
            self.config.set(
                'UEVaultManager',
                '; Create a backup of the output file (when using the --output option) suffixed by a timestamp before creating a new file'
            )
            self.config.set('UEVaultManager', 'create_output_backup', 'True')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'create_log_backup'):
            self.config.set(
                'UEVaultManager', '; Set to True to create a backup of the log files that store asset analysis. It is suffixed by a timestamp'
            )
            self.config.set('UEVaultManager', 'create_log_backup', 'True')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'verbose_mode'):
            self.config.set('UEVaultManager', '; Set to True to print more information during long operations')
            self.config.set('UEVaultManager', 'verbose_mode', 'False')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'ue_assets_max_cache_duration'):
            self.config.set('UEVaultManager', '; Delay in seconds when UE assets metadata cache will be invalidated. Default value represent 15 days')
            self.config.set('UEVaultManager', 'ue_assets_max_cache_duration', '1296000')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'ignored_assets_filename_log'):
            self.config.set(
                'UEVaultManager', '; File name (and path) to log issues with assets when running the --list command' + "\n" +
                '; use "~/" at the start of the filename to store it relatively to the user directory'
            )
            self.config.set('UEVaultManager', 'ignored_assets_filename_log', '~/.config/ignored_assets.log')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'notfound_assets_filename_log'):
            self.config.set('UEVaultManager', 'notfound_assets_filename_log', '~/.config/notfound_assets.log')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'bad_data_assets_filename_log'):
            self.config.set('UEVaultManager', 'bad_data_assets_filename_log', '~/.config/bad_data_assets.log')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'scan_assets_filename_log'):
            self.config.set('UEVaultManager', 'scan_assets_filename_log', '~/.config/scan_assets.log')
            has_changed = True
        if not self.config.has_option('UEVaultManager', 'engine_version_for_obsolete_assets'):
            self.config.set('UEVaultManager', '; Minimal unreal engine version to check for obsolete assets (default is 4.26)')
            self.config.set(
                'UEVaultManager', 'engine_version_for_obsolete_assets', '4.26'
            )  # no access to the engine_version_for_obsolete_assets global settings here without importing its module
            has_changed = True

        if has_changed:
            self.save_config()

        # load existing installed assets
        self._installed_assets = {}
        self.load_installed_assets()

        # load asset sizes
        try:
            with open(self.asset_sizes_filename, 'r', encoding='utf-8') as file:
                self._asset_sizes = json.load(file)
        except Exception as error:
            self.log.debug(f'Loading assets sizes failed: {error!r}')
            self._asset_sizes = None

        # load existing assets metadata
        _meta = None
        for gm_file in os.listdir(path_join(self.metadata_folder)):
            try:
                with open(path_join(self.metadata_folder, gm_file), 'r', encoding='utf-8') as file:
                    _meta = json.load(file)
                    self.assets_metadata[_meta['app_name']] = _meta
            except Exception as error:
                self.log.debug(f'Loading asset meta file "{gm_file}" failed: {error!r}')

        # done when asset metadata is parsed to allow filtering
        # load existing Asset extra data
        # for gm_file in os.listdir(self.extra_folder):
        #    try:
        #        _extra = json.load(open(path_join(self.extra_folder, gm_file)))
        #        self._assets_extra_data[_extra['asset_name']] = _extra
        #    except Exception as error:
        #        self.log.debug(f'Loading asset extra file "{gm_file}" failed: {error!r}')

        # not used anymore
        # load auto-aliases if enabled
        # self.aliases = {}
        # if not self.config.getboolean('UEVaultManager', 'disable_auto_aliasing', fallback=False):
        #     try:
        #         _j = json.load(open(path_join(self.path, 'aliases.json')))
        #         for app_name, aliases in _j.items():
        #             for alias in aliases:
        #                 self.aliases[alias] = app_name
        #     except Exception as error:
        #         self.log.debug(f"Loading aliases failed with {error!r}")

    @property
    def userdata(self):
        """
        Return the user data as a dict.
        :return: user data.
        """
        if self._user_data is not None:
            return self._user_data
        try:
            with open(self.user_data_filename, 'r', encoding='utf-8') as file:
                self._user_data = json.load(file)
        except Exception as error:
            self.log.debug(f'Failed to load user data: {error!r}')
            return None
        return self._user_data

    @userdata.setter
    def userdata(self, userdata: dict) -> None:
        """
        Set the user data.
        :param userdata: user data.
        """
        if userdata is None:
            raise ValueError('Userdata is none!')

        self._user_data = userdata
        with open(self.user_data_filename, 'w', encoding='utf-8') as file:
            json.dump(userdata, file, indent=2, sort_keys=True)

    def invalidate_userdata(self) -> None:
        """
        Invalidate the user data.
        """
        self._user_data = None
        if os.path.exists(self.user_data_filename):
            os.remove(self.user_data_filename)

    @property
    def assets(self):
        """
        Return the asset's data as a dict. If not loaded, load it from the json file.
        :return: asset's data.
        """
        if self._assets is None:
            try:
                with open(self.assets_data_filename, 'r', encoding='utf-8') as file:
                    tmp = json.load(file)
                    self._assets = {k: [AssetBase.from_json(j) for j in v] for k, v in tmp.items()}
            except Exception as error:
                self.log.debug(f"Failed to load asset's data: {error!r}")
        return self._assets

    @assets.setter
    def assets(self, assets) -> None:
        """
        Set the asset data and saved it to a json file.
        :param assets: assets.
        """
        if assets is None:
            raise ValueError('No Assets data!')
        self._assets = assets
        with open(self.assets_data_filename, 'w', encoding='utf-8') as file:
            json.dump({platform: [a.__dict__ for a in assets] for platform, assets in self._assets.items()}, file, indent=2, sort_keys=True)

    @property
    def asset_sizes(self):
        """
        Return the asset's sizes as a dict. If not loaded, load it from the json file.
        :return: asset's size.
        """
        if self._asset_sizes is None:
            try:
                with open(self.asset_sizes_filename, 'r', encoding='utf-8') as file:
                    self._asset_sizes = json.load(file)
            except Exception as error:
                self.log.debug(f"Failed to load asset's size: {error!r}")
        return self._asset_sizes

    @asset_sizes.setter
    def asset_sizes(self, asset_sizes) -> None:
        """
        Set the asset data and saved it to a json file.
        :param asset_sizes: asset sizes.
        """
        self._asset_sizes = asset_sizes
        with open(self.asset_sizes_filename, 'w', encoding='utf-8') as file:
            json.dump(self._asset_sizes, file, indent=2, sort_keys=True)

    @staticmethod
    def load_filter_list(filename: str = '') -> Optional[dict]:
        """
        Load the filters from a json file
        :return: the filters or {} if not found. Will return None on error
        """
        filename = filename or gui_g.s.last_opened_filter
        folder = gui_g.s.filters_folder
        full_filename = path_join(folder, filename)
        if not os.path.isfile(full_filename):
            return {}
        try:
            with open(full_filename, 'r', encoding='utf-8') as file:
                filters = json.load(file)
        except (Exception, ):
            return None
        return filters

    @staticmethod
    def save_filter_list(filters: {}, filename: str = '') -> None:
        """
        Save the filters to a json file.
        """
        filename = filename or gui_g.s.last_opened_filter
        folder = gui_g.s.filters_folder
        full_filename = path_join(folder, filename)
        if not full_filename:
            return
        with open(full_filename, 'w', encoding='utf-8') as file:
            json.dump(filters, file, indent=2, sort_keys=True)

    def _get_manifest_filename(self, app_name: str, version: str, platform: str = None) -> str:
        """
        Get the manifest filename.
        :param app_name: Asset name.
        :param version: version of the manifest.
        :param platform: platform of the manifest.
        :return: the manifest filename.
        """
        if platform:
            fname = clean_filename(f'{app_name}_{platform}_{version}')
        else:
            fname = clean_filename(f'{app_name}_{version}')
        return path_join(self.manifests_folder, f'{fname}.manifest')

    def delete_folder_content(self, folders=None, extensions_to_delete: list = None, file_name_to_keep: list = None) -> int:
        """
        Delete all the files in a folder that are not in the list_of_items_to_keep list.
        :param folders: the list of folder to clean. Could be a list or a string for a single folder.If None, the function will return 0.
        :param extensions_to_delete: the list of extensions to delete. Leave to Empty to delete all extentions.
        :param file_name_to_keep: the list of items to keep. Leave to Empty to delete all files.
        :return: the total size of deleted files.
        """
        if not folders:
            return 0
        if isinstance(folders, str):
            folders_to_clean = [folders]
        else:
            folders_to_clean = folders

        if len(folders_to_clean) < 1:
            return 0
        if file_name_to_keep is None:
            file_name_to_keep = []
        size_deleted = 0
        while folders_to_clean:
            folder = folders_to_clean.pop()
            if folder == self.path and extensions_to_delete is None:
                self.log.warning("We can't delete the config folder without extensions to filter files!")
                continue
            if not os.path.isdir(folder):
                continue
            for f in os.listdir(folder):
                file_name = path_join(folder, f)
                # file_name = os.path.abspath(file_name)
                app_name, file_ext = os.path.splitext(f)
                file_ext = file_ext.lower()
                file_is_ok = (file_name_to_keep is None or app_name not in file_name_to_keep)
                ext_is_ok = (extensions_to_delete is None or file_ext in extensions_to_delete)
                if file_is_ok and ext_is_ok:
                    try:
                        size = os.path.getsize(file_name)
                        os.remove(file_name)
                        size_deleted += size
                    except Exception as error:
                        self.log.warning(f'Failed to delete file "{file_name}": {error!r}')
                elif os.path.isdir(file_name):
                    folders_to_clean.append(file_name)
        return size_deleted

    def load_manifest(self, app_name: str, version: str, platform: str = 'Windows') -> any:
        """
        Load the manifest data from a file.
        :param app_name: the name of the item.
        :param version: version of the manifest.
        :param platform: platform of the manifest.
        :return: the manifest data.
        """
        try:
            return open(self._get_manifest_filename(app_name, version, platform), 'rb').read()
        except FileNotFoundError:  # all other errors should propagate
            self.log.debug(f'Loading manifest failed, retrying without platform in filename...')
            try:
                return open(self._get_manifest_filename(app_name, version), 'rb').read()
            except FileNotFoundError:  # all other errors should propagate
                return None

    def save_manifest(self, app_name: str, manifest_data, version: str, platform: str = 'Windows') -> str:
        """
        Save the manifest data to a file.
        :param app_name: the name of the item.
        :param manifest_data: the manifest data.
        :param version: version of the manifest.
        :param platform: platform of the manifest.
        :return: the manifest filename.
        """
        filename = self._get_manifest_filename(app_name, version, platform)
        with open(filename, 'wb') as file:
            file.write(manifest_data)
        return filename

    def get_item_meta(self, app_name: str) -> Optional[Asset]:
        """
        Get the metadata for an item.
        :param app_name: the name of the item.
        :return: an Asset object.
        """
        # Note: self._assets_metadata is filled at the start of the list command by reading all the json files in the metadata folder
        if _meta := self.assets_metadata.get(app_name, None):
            return Asset.from_json(_meta)  # create an object from the Asset class using the json data
        return None

    def set_item_meta(self, app_name: str, meta) -> None:
        """
        Set the metadata for an item.
        :param app_name: the name of the item.
        :param meta: the metadata object.
        """
        json_meta = meta.__dict__
        self.assets_metadata[app_name] = json_meta
        meta_file = path_join(self.metadata_folder, f'{app_name}.json')
        with open(meta_file, 'w', encoding='utf-8') as file:
            json.dump(json_meta, file, indent=2, sort_keys=True)

    def delete_item_meta(self, app_name: str) -> None:
        """
        Delete the metadata for an item.
        :param app_name: the name of the item.
        """
        if app_name not in self.assets_metadata:
            raise ValueError(f'Item {app_name} does not exist in metadata DB!')

        del self.assets_metadata[app_name]
        meta_file = path_join(self.metadata_folder, f'{app_name}.json')
        if os.path.exists(meta_file):
            os.remove(meta_file)

    def get_item_extra(self, app_name: str) -> dict:
        """
        Get the extra data for an Asset.
        :param app_name: the Asset name.
        :return: the extra data.
        """
        extra = self.assets_extra_data.get(app_name, None)
        extra_file = path_join(self.extra_folder, f'{app_name}.json')
        if extra is None and os.path.exists(extra_file):
            try:
                with open(extra_file, 'r', encoding='utf-8') as file:
                    extra = json.load(file)
                    self.assets_extra_data[extra['asset_name']] = extra
            except json.decoder.JSONDecodeError:
                self.log.warning(f'Failed to load extra data for {app_name}!. Deleting file...')
                # delete the file
                try:
                    os.remove(extra_file)
                except Exception as error:
                    self.log.error(f'Failed to delete extra file {extra_file}: {error!r}')
                return {}
        return extra

    def set_item_extra(self, app_name: str, extra: dict, update_global_dict: True) -> None:
        """
        Save the extra data for an Asset.
        :param app_name: the Asset name.
        :param extra: the extra data.
        :param update_global_dict: update the global dict with the new data.
        """
        extra_file = path_join(self.extra_folder, f'{app_name}.json')
        self.log.debug(f'--- SAVING {len(extra)} extra data for {app_name} in {extra_file}')
        with open(extra_file, 'w', encoding='utf-8') as file:
            json.dump(extra, file, indent=2, sort_keys=True)
        if update_global_dict:
            self.assets_extra_data[app_name] = extra

    def delete_item_extra(self, app_name: str, update_global_dict: True) -> None:
        """
        Delete the extra data for an Asset.
        :param app_name: the Asset name.
        :param update_global_dict: update the global dict with the new data.
        """
        if update_global_dict and self.assets_extra_data.get(app_name):
            del self.assets_extra_data[app_name]
        extra_file = path_join(self.extra_folder, f'{app_name}.json')
        if os.path.exists(extra_file):
            os.remove(extra_file)

    def get_item_app_names(self) -> list:
        """
        Get the list of Asset names.
        :return: the list of Asset names.
        """
        return sorted(self.assets_metadata.keys())

    def clean_tmp_data(self) -> int:
        """
        Delete all the files in the tmp folder.
        :return: the size of the deleted files.
        """
        return self.delete_folder_content(self.tmp_folder)

    def clean_cache_data(self) -> int:
        """
        Delete all the files in the cache folders.
        :return: the size of the deleted files.
        """
        return self.delete_folder_content(gui_g.s.cache_folder)

    def clean_metadata(self, names_to_keep: list) -> int:
        """
        Delete all the metadata files that are not in the names_to_keep list.
        :param names_to_keep: the list of asset names to keep.
        :return: the size of the deleted files.
        """
        return self.delete_folder_content(self.metadata_folder, file_name_to_keep=names_to_keep)

    def clean_extra(self, names_to_keep: list) -> int:
        """
        Delete all the metadata files that are not in the names_to_keep list.
        :param names_to_keep: the list of asset names to keep.
        :return: the size of the deleted files.
        """
        return self.delete_folder_content(self.extra_folder, file_name_to_keep=names_to_keep)

    def clean_manifests(self) -> int:
        """
        Delete all the metadata files that are not in the names_to_keep list.
        """
        return self.delete_folder_content(self.manifests_folder)

    def clean_logs_and_backups(self) -> int:
        """
        Delete all the log and backup files in the application folders.
        :return: the size of the deleted files.
        """
        folders = [self.path, gui_g.s.results_folder, gui_g.s.scraping_folder]
        return self.delete_folder_content(folders, ['.log', '.bak'])

    def load_installed_assets(self) -> bool:
        """
        Get the installed asset data.
        :return: True if the asset data is loaded.
        """
        try:
            with open(self.installed_asset_filename, 'r', encoding='utf-8') as file:
                self._installed_assets = json.load(file)
        except Exception as error:
            self.log.debug(f'Failed to load installed asset data: {error!r}')
            return False
        has_changed = False
        for asset in self._installed_assets.values():
            installed_folders = asset.get('installed_folders', None)
            if installed_folders is None:
                asset['installed_folders'] = []
            else:
                # remove all empty string in installed_folders
                asset['installed_folders'] = [folder for folder in asset['installed_folders'] if str(folder).strip()]
            has_changed = has_changed or installed_folders != asset['installed_folders']

        if has_changed:
            self.save_installed_assets()

    def save_installed_assets(self) -> None:
        """
        Save the installed asset data.
        """
        installed_assets = self._installed_assets
        with open(self.installed_asset_filename, 'w', encoding='utf-8') as file:
            json.dump(installed_assets, file, indent=2, sort_keys=True)

    def get_installed_asset(self, app_name: str) -> Optional[InstalledAsset]:
        """
        Get the installed asset data. If it's not currently loaded, it will be read from the json file
        :param app_name: the asset name.
        :return: the installed asset or None if not found.
        """
        if not app_name:
            return None

        if not self._installed_assets:
            self.load_installed_assets()

        json_data = self._installed_assets.get(app_name)
        if json_data:
            return InstalledAsset.from_json(json_data)

        return None

    def remove_installed_asset(self, app_name: str) -> None:
        """
        Remove an installed asset from the list.
        :param app_name: the asset name.
        :return:
        """
        if app_name and app_name in self._installed_assets:
            del self._installed_assets[app_name]
            self.save_installed_assets()

    def update_installed_asset(self, app_name: str, asset_data: dict = None) -> None:
        """
        Update an installed asset data.
        :param app_name: the asset name.
        :param asset_data: the installed asset data.
        """
        if not app_name:
            return
        if not self._installed_assets:
            self._installed_assets = {}
        has_changed = True
        if asset_data is not None:
            if app_name in self._installed_assets:
                asset_existing = self._installed_assets[app_name]
                # merge the installed_folders fields
                installed_folders_existing = asset_existing.get('installed_folders', [])
                installed_folders_added = asset_data.get('installed_folders', [])
                installed_folders_merged = merge_lists_or_strings(installed_folders_existing, installed_folders_added)
                if installed_folders_merged != installed_folders_existing:
                    asset_data['installed_folders'] = installed_folders_merged
                    self._installed_assets[app_name].update(asset_data)
                else:
                    has_changed = False
            else:
                self._installed_assets[app_name] = asset_data
        else:
            return
        if has_changed:
            self.save_installed_assets()

    def set_installed_asset(self, installed_asset: InstalledAsset) -> None:
        """
        Set the installed asset. Will not create the list if it doesn't exist. Use add_to_installed_assets() instead.
        :param installed_asset: the installed asset to set.
        """
        app_name = installed_asset.app_name
        if not app_name or app_name not in self._installed_assets:
            return
        self._installed_assets[app_name] = installed_asset.__dict__

    def add_to_installed_assets(self, installed_asset: InstalledAsset) -> bool:
        """
        Add an installed asset to the list.
        :param installed_asset: the installed asset to add.
        :return: True if the asset was added.
        """
        if not self._installed_assets:
            self._installed_assets = {}
        app_name = installed_asset.app_name
        if app_name not in self._installed_assets:
            self._installed_assets[app_name] = installed_asset.__dict__
            return True
        return False

    def get_installed_assets(self) -> dict:
        """
        Get the installed asset data.
        :return: the installed asset data.
        """
        return self._installed_assets

    def get_asset_size(self, app_name: str) -> int:
        """
        Get the size of an asset.
        :param app_name: the asset name.
        :return: the size of the asset. -1 if not found.
        """
        if not app_name:
            return 0
        return self._asset_sizes.get(app_name, -1)

    def set_asset_size(self, app_name: str, size: int) -> None:
        """
        Set the size of an asset.
        :param app_name: the asset name.
        :param size: the size of the asset
        """
        if not app_name:
            return
        if self._asset_sizes is None:
            self._asset_sizes = {}
        self._asset_sizes[app_name] = size
        with open(self.asset_sizes_filename, 'w', encoding='utf-8') as file:
            json.dump(self._asset_sizes, file, indent=2, sort_keys=True)

    def save_config(self) -> None:
        """
        Save the config file.
        """
        # do not save if in read-only mode or file hasn't changed
        if self.config.read_only or not self.config.modified:
            return

        file_backup = create_file_backup(self.config_file)
        with open(self.config_file, 'w', encoding='utf-8') as file:
            self.config.write(file)
        # delete the backup if the files and the backup are identical
        if os.path.isfile(file_backup) and filecmp.cmp(self.config_file, file_backup):
            os.remove(file_backup)

    def clean_scrapping(self) -> int:
        """
        Delete all the metadata files that are not in the names_to_keep list.
        :return: the size of the deleted files.
        """
        folders = [gui_g.s.assets_data_folder, gui_g.s.owned_assets_data_folder, gui_g.s.assets_global_folder, gui_g.s.assets_csv_files_folder]
        return self.delete_folder_content(folders)

    def get_online_version_saved(self) -> dict:
        """
        Get the cached version data.
        :return: version data.
        """
        if self._update_info:
            return self._update_info
        try:
            with open(self.online_version_filename, 'r', encoding='utf-8') as file:
                self._update_info = json.load(file)
        except Exception as error:
            self.log.debug(f'Failed to load cached version data: {error!r}')
            self._update_info = dict(last_update=0, data=None)
        return self._update_info

    def set_online_version_saved(self, version_data: dict) -> None:
        """
        Set the cached version data.
        :param version_data: the version data.
        """
        if not version_data:
            return
        self._update_info = dict(last_update=time(), data=version_data)
        with open(self.online_version_filename, 'w', encoding='utf-8') as file:
            json.dump(self._update_info, file, indent=2, sort_keys=True)

    def get_assets_cache_info(self) -> dict:
        """
        Get assets metadata cache information.
        :return: dict {last_update, ue_assets_count}.
        """
        if self._assets_cache_info:
            return self._assets_cache_info
        try:
            with open(self.assets_cache_info_filename, 'r', encoding='utf-8') as file:
                self._assets_cache_info = json.load(file)
        except Exception as error:
            self.log.debug(f'Failed to UE assets last update data: {error!r}')
            self._assets_cache_info = dict(last_update=0, ue_assets_count=0)
        return self._assets_cache_info

    def set_assets_cache_info(self, last_update: float, ue_assets_count: int) -> None:
        """
        Set assets metadata cache information.
        :param last_update: last update time.
        :param ue_assets_count: number of UE assets on last update.
        :return:
        """
        self._assets_cache_info = dict(last_update=last_update, ue_assets_count=ue_assets_count)
        with open(self.assets_cache_info_filename, 'w', encoding='utf-8') as file:
            json.dump(self._assets_cache_info, file, indent=2, sort_keys=True)

    def extract_version_from_releases(self, release_info: dict) -> (dict, str):
        """
        Extract the version list and the release dict from the release info.
        :param release_info: the release info (from the asset info).
        :return: (the release dict, the id of the latest release).
        """
        releases = {}
        all_installed_folders = {}
        installed_assets = self.get_installed_assets()
        latest_id = ''
        for asset_id, installed_asset in installed_assets.items():
            all_installed_folders[asset_id] = installed_asset['installed_folders']
        if release_info is not None and len(release_info) > 0:
            # TODO: only keep releases that are compatible with the version of the selected project or engine.
            for index, item in enumerate(reversed(release_info)):  # reversed to have the latest release first
                asset_id = item.get('appId', None)
                latest_id = latest_id or asset_id
                release_title = item.get('versionTitle', '') or asset_id
                compatible_list = item.get('compatibleApps', None)
                date_added = item.get('dateAdded', '')
                # Convert the string to a datetime object
                datetime_obj = datetime.strptime(date_added, "%Y-%m-%dT%H:%M:%S.%fZ")
                # Format the datetime object as "YYYY-MM-DD"
                formatted_date = datetime_obj.strftime('%Y-%m-%d')
                if asset_id is not None and release_title is not None and compatible_list is not None:
                    # remove 'UE_' from items of the compatible_list
                    compatible_list = [item.replace('UE_', '') for item in compatible_list]
                    data = {
                        # 'id': asset_id,  # duplicate with the dict key
                        'title': release_title,  #
                        'compatible': compatible_list,  #
                    }
                    compatible_str = ','.join(compatible_list)
                    desc = f'Release id: {asset_id}\nTitle: {release_title}\nRelease Date: {formatted_date}\nUE Versions: {compatible_str}'
                    folder_choice = {}
                    if all_installed_folders.get(asset_id, ''):
                        data['installed_folders'] = all_installed_folders.get(asset_id, [])
                        desc += f'\nInstalled in folders:\n'
                        # add each folder to the description
                        for folder in data['installed_folders']:
                            desc += f' - {folder}\n'
                            # create a sublist of folders for the version choice list
                            # generate a comprehensive label from the full path of a folder
                            # (ex: C:\Program Files\Epic Games\UE_4.27\Engine\Plugins\Marketplace\MyAsset)
                            # to be used in the version choice list
                            # (ex: MyAsset (4.27))
                            label = generate_label_from_path(folder)
                            folder_choice.update(
                                {
                                    label: {
                                        # 'id': label, # duplicate with the dict key
                                        'value': folder,  #
                                        'text': 'Select the installation folder to remove',  #
                                    }
                                }
                            )
                    data['desc'] = desc
                    data['content'] = folder_choice
                    releases[asset_id] = data
        return releases, latest_id

    def get_downloaded_assets_data(self, vault_cache_folder: str, max_depth: int = 3) -> dict:
        """
        Get the list of the assets in the Vault cache folder. Get its size from the installed_asset file if it exists.
        :param vault_cache_folder: the Vault cache folder.
        :param max_depth: maximum depth of subfolders to include in the file list.
        :return: dict {asset_id: {size, path}}

        NOTES:
        The scan of a Vault cache folder with lots of assets can take a long time.
        This scan is done when the datatable is loaded.
        So, increase the max_depth value with care to avoid long loading times.
        """
        vault_cache_folder = os.path.normpath(vault_cache_folder)
        downloaded_assets = {}
        # scan the vault_cache_folder for files. Proceed level by level until max_depth is reached.
        for root, dirs, files in os.walk(vault_cache_folder):
            # print(f'scanning root: {root}')
            depth = root[len(vault_cache_folder) + len(os.path.sep):].count(os.path.sep)
            if depth == max_depth:
                # remove all subfolders from the list of folders to scan to speed up the process
                del dirs[:]
            for file in files:
                filename, _ = os.path.splitext(file)
                # print(f'root: {root}, file: {file}, filename: {filename}')
                if filename.lower() == gui_g.s.ue_manifest_filename.lower():
                    # print('==>found manifest file')
                    parts = root.split(os.sep)
                    asset_id = parts[-1]  # the folder name is the asset id
                    installed_asset = self.get_installed_asset(asset_id)
                    size = installed_asset.install_size if installed_asset else 1
                    file_path = os.path.join(root, file)
                    downloaded_assets[asset_id] = {'size': size, 'path': file_path}
        return downloaded_assets
