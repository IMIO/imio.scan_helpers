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
from utils import get_latest_release_version
from utils import get_version
from utils import stop

import argparse
import os


GITHUB_REPO = "IMIO/imio.scan_helpers"
DOWNLOAD_DIR = "_downloads"
EXECUTABLE_NAME = "main.exe"


def check_for_updates():
    """Check for updates"""
    current_version = get_version()
    latest_version, download_url = get_latest_release_version(GITHUB_REPO, ns.release)
    stop(f"Current version: {current_version}\nLatest version: {latest_version}\nDownload URL: {download_url}")


# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", action="store_true", dest="version", help="Show version")
parser.add_argument("-nu", "--no-update", action="store_true", dest="no_update", help="Do not check for updates")
parser.add_argument("-r", "--release", dest="release", help="Get this release")
ns = parser.parse_args()

if ns.version:
    stop("imio.scan_helpers version {}".format(get_version()), False)
if not ns.no_update:
    check_for_updates()
# will restore some files
pass
