# -*- mode: python ; coding: utf-8 -*-
import shutil


a = Analysis(
    ['imio/scan_helpers/main.py'],
    pathex=['imio/scan_helpers'],
    binaries=[],
    datas=[("imio/scan_helpers/version.txt", ".")],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe0 = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe0,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='imio-scan-helpers',
)

# Archive everything into a zip file
print('Creating zip file')
shutil.make_archive('dist/imio-scan-helpers', 'zip', 'dist/imio-scan-helpers')
