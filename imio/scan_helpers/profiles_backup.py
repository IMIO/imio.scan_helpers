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
from logger import log
from utils import get_main_backup_dir
from utils import get_scan_profiles_dir
from utils import read_dir
from utils import stop

import argparse
from datetime import datetime


# Argument parsing
parser = argparse.ArgumentParser()
# parser.add_argument("-v", "--version", action="store_true", dest="version", help="Show version")
# parser.add_argument("-r", "--release", dest="release", help="Get this release")
ns = parser.parse_args()

log.info(f"Starting backup script")
main_prof_dir = get_scan_profiles_dir()
prof_dirs = read_dir(main_prof_dir, with_path=True, only_folders=True)
if not prof_dirs:
    stop(f"No profiles found in '{main_prof_dir}'")
main_backup_dir = get_main_backup_dir()
day = datetime.now().strftime("%Y-%m-%d")

