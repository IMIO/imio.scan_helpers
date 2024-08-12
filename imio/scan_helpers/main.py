#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the imio.scan_helpers distribution (https://github.com/IMIO/imio.scan_helpers).
# Copyright (c) 2023 IMIO
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
from config import get_bundle_dir
from config import get_current_version
from config import MAIN_EXE_NAME
from config import PARAMS_FILE_NAME
from logger import close_logger
from logger import log
from utils import copy_release_files_and_restart
from utils import download_update
from utils import get_download_dir_path
from utils import get_latest_release_version
from utils import get_parameter
from utils import send_log_message
from utils import stop
from utils import store_client_id
from utils import unzip_file

import argparse
import os


def handle_startup(main_dir, clientid, action="add"):
    """Add/remove exe to/from startup"""
    exe_path = os.path.join(main_dir, f"{MAIN_EXE_NAME}.exe")
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    value_name = "IMIO_Scan_Helpers_Scripts"
    try:
        import winreg

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_SET_VALUE) as reg_key:
            if action == "add":
                winreg.SetValueEx(reg_key, value_name, 0, winreg.REG_SZ, exe_path)
                log.info(f"'{exe_path}' added to startup")
            elif action == "remove":
                winreg.DeleteValue(reg_key, value_name)
                log.info(f"'{exe_path}' removed from startup")
    except ImportError as e:
        send_log_message(f"Cannot import winreg: add to startup failed !!", clientid)
    except Exception as e:
        send_log_message(f"Error in handle_startup : {e}", clientid)


def check_for_updates(main_dir, clientid):
    """Check for updates"""
    current_version = get_current_version()
    latest_version, download_url = get_latest_release_version(clientid, ns.release)
    if latest_version > current_version or ns.release:
        log.info(f"New version available: {latest_version}")
        download_dir_path = get_download_dir_path()
        if not os.path.exists(download_dir_path):
            os.makedirs(download_dir_path)
        download_path = os.path.join(download_dir_path, download_url.split("/")[-1])
        log.info(f"Downloading {download_url} to {download_path}")
        download_update(download_url, download_path)
        log.info(f"Unzipping {download_path} to {download_dir_path}")
        unzip_file(download_path, download_dir_path)
        copy_release_files_and_restart(download_dir_path, main_dir)
        log.info("Will replace files and restart")
        stop(intup=False)


# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", action="store_true", dest="version", help="Show version")
parser.add_argument("-c", "--client-id", dest="client_id", help="Set client id")
parser.add_argument("-nu", "--no-update", action="store_true", dest="no_update", help="Do not check for updates")
parser.add_argument("-r", "--release", dest="release", help="Get this release")
parser.add_argument("--startup", action="store_true", dest="startup", help="Add exe to startup")
parser.add_argument("--startup-remove", action="store_true", dest="startup_remove", help="Remove exe from startup")
ns = parser.parse_args()

if ns.version:
    print(f"imio.scan_helpers version {get_current_version()}")
    stop(intup=False)
bundle_dir = get_bundle_dir()
log.info(f"dir={bundle_dir}")
params_file = os.path.join(bundle_dir, PARAMS_FILE_NAME)
if ns.client_id:
    store_client_id(params_file, ns.client_id)
client_id = get_parameter(params_file, "CLIENT_ID")
try:
    if ns.startup:
        handle_startup(bundle_dir, client_id)
    if ns.startup_remove:
        handle_startup(bundle_dir, client_id, action="remove")
    if ns.no_update:
        # remove bat file
        pass
    else:
        check_for_updates(bundle_dir, client_id)
except Exception as ex:
    send_log_message(f"General error in main script '{ex}'", client_id)

# will do something
log.info(f"Current version is {get_current_version()}")
log.info("Nothing to do actually")
close_logger()
