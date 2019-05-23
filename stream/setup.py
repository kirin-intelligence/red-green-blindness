from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('setup.py', base=base)
]

setup(name='main',
      version = '1.0',
      description = 'main',
      options = dict(build_exe = buildOptions),
      executables = executables)
