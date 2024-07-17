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
from config import BUNDLE_NAME
from config import DOWNLOAD_DIR
from config import GITHUB_REPO
from config import INTERNAL_DIR

import os
import requests
import shutil
import sys
import zipfile


BUNDLE_DIR = os.path.dirname(__file__)
if os.path.basename(BUNDLE_DIR) == INTERNAL_DIR:
    BUNDLE_DIR = os.path.dirname(BUNDLE_DIR)


def copy_files(src_dir, dest_dir):
    for item in os.listdir(src_dir):
        if item.startswith(BUNDLE_NAME) and item.endswith(".zip"):
            continue
        s = os.path.join(src_dir, item)
        d = os.path.join(dest_dir, item)
        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)


def download_update(url, download_path):
    """Download github zip file"""
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(download_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)


def get_bundle_dir():
    if os.path.exists(os.path.join(BUNDLE_DIR, INTERNAL_DIR)):
        return BUNDLE_DIR
    else:  # dev mode
        root_dir = os.path.dirname(os.path.dirname(BUNDLE_DIR))
        if os.path.exists(os.path.join(root_dir, "dist", BUNDLE_NAME)):
            return os.path.join(root_dir, "dist", BUNDLE_NAME)
        elif os.path.exists(os.path.join(root_dir, "dist")):
            return os.path.join(root_dir, "dist")
        return root_dir


def get_download_dir_path():
    # maybe use tempdir
    # temp_dir = tempfile.gettempdir()
    return os.path.join(get_bundle_dir(), DOWNLOAD_DIR)


def get_current_version():
    """Get current version"""
    if os.path.exists(os.path.join(BUNDLE_DIR, INTERNAL_DIR, "version.txt")):
        v_path = os.path.join(BUNDLE_DIR, INTERNAL_DIR, "version.txt")
    elif os.path.exists(os.path.join(BUNDLE_DIR, "version.txt")):  # dev mode
        v_path = os.path.join(BUNDLE_DIR, "version.txt")
    with open(v_path, "r") as file:
        return file.readline().strip()


def get_latest_release_version(release=None):
    """Get github latest or specified release info"""
    if release:
        url = f"https://api.github.com/repos/{GITHUB_REPO}/releases"
        ret = json_request(url)
        for dic in ret:
            if dic["tag_name"] == release:
                url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/{dic['id']}"
                break
        else:
            stop(f"The release with tag '{release}' cannot be found")
    else:
        url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
    response = requests.get(url)
    response.raise_for_status()
    latest_release = response.json()
    return latest_release["tag_name"], latest_release["assets"][0]["browser_download_url"]


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


def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
