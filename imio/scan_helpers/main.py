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
from utils import copy_files
from utils import download_update
from utils import get_bundle_dir
from utils import get_download_dir_path
from utils import get_latest_release_version
from utils import get_current_version
from utils import stop
from utils import unzip_file

import argparse
import os
import subprocess
import sys


def check_for_updates():
    """Check for updates"""
    current_version = get_current_version()
    latest_version, download_url = get_latest_release_version(ns.release)
    if latest_version > current_version:
        print(f"New version available: {latest_version}")
        download_dir_path = get_download_dir_path()
        if not os.path.exists(download_dir_path):
            os.makedirs(download_dir_path)
        download_path = os.path.join(download_dir_path, download_url.split("/")[-1])
        print(f"Downloading {download_url} to {download_path}")
        download_update(download_url, download_path)
        print(f"Unzipping {download_path} to {download_dir_path}")
        unzip_file(download_path, download_dir_path)
        bundle_dir = get_bundle_dir()
        print(f"Copying files from {download_dir_path} to {bundle_dir}")
        copy_files(download_dir_path, bundle_dir)
        print("Will replace files and restart")
        sys.exit(0)


# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", action="store_true", dest="version", help="Show version")
parser.add_argument("-nu", "--no-update", action="store_true", dest="no_update", help="Do not check for updates")
parser.add_argument("-r", "--release", dest="release", help="Get this release")
ns = parser.parse_args()

if ns.version:
    stop("imio.scan_helpers version {}".format(get_current_version()), False)
if not ns.no_update:
    check_for_updates()

# will do something
stop("Doing something after update")
