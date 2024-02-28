# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
  datas=[
    ('shape_predictor_5_face_landmarks.dat', 'face_recognition_models/models'),
    ('shape_predictor_68_face_landmarks.dat', 'face_recognition_models/models'),
    ('mmod_human_face_detector.dat','face_recognition_models/models'),
    ('dlib_face_recognition_resnet_model_v1.dat','face_recognition_models/models')
	],
	hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
