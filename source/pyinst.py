import PyInstaller.__main__

PyInstaller.__main__.run([
    'run.py',
    '--onefile',
    '--icon=icon.ico',
    '--hidden-import=requests',
    '--hidden-import=PIL',
    '--add-data=guython:guython'
])
