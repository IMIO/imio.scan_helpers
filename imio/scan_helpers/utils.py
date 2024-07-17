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

import requests
import sys


BUNDLE_DIR = path.dirname(__file__)


def get_latest_release_version(github_repo, release=None):
    """Get github latest or specified release info"""
    if release:
        url = f"https://api.github.com/repos/{github_repo}/releases"
        ret = json_request(url)
        for dic in ret:
            if dic["tag_name"] == release:
                url = f"https://api.github.com/repos/{github_repo}/releases/{dic['id']}"
                break
        else:
            stop(f"The release with tag '{release}' cannot be found")
    else:
        url = f"https://api.github.com/repos/{github_repo}/releases/latest"
    response = requests.get(url)
    response.raise_for_status()
    latest_release = response.json()
    return latest_release["tag_name"], latest_release["assets"][0]["browser_download_url"]


def get_version():
    with open('{}/version.txt'.format(BUNDLE_DIR), 'r') as file:
        return file.readline().strip()


def json_request(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def stop(msg="", intup=True):
    if msg:
        print(msg)
    if intup:
        input("Press Enter to exit...")
    sys.exit(0)
