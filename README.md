# imio.scan_helpers
Various script files to handle MS Windows scan tool

## Installation
Use virtualenv in bin directory destination

## Build locally
bin/pyinstaller -y imio-scan-helpers.spec

## github actions
On each push or tag, the github action will build the package and upload it to the github release page.
https://github.com/IMIO/imio.scan_helpers/releases

## Windows installation
The zip archive must be decompressed in a directory.

## Windows usage

* main.exe -h : displays the help
* main.exe -u : updates the software
