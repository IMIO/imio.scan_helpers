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

from os import path

import sys


BUNDLE_DIR = path.dirname(__file__)


def get_version():
    with open('{}/version.txt'.format(BUNDLE_DIR), 'r') as file:
        return file.readline().strip()


def stop(msg="", intup=True):
    if msg:
        print(msg)
    if intup:
        input("Press Enter to exit...")
    sys.exit(0)
