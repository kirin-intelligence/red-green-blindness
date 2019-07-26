import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_exe_options = {
    "include_files": ["lib", 'image', 'python36.dll'],
    "packages": ["pyqt5","os", "sys"], "excludes": []}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "win32gui"
product_name = u'交通拥堵分析系统'.encode('gbk')
exec_name = u'交通拥堵分析系统.exe'.encode('gbk')
product_name='Transport'
exec_name='Transport'
shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "program",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]Transport.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     'TARGETDIR'  # WkDir
     ),

    ("StartupShortcut",  # Shortcut
     "StartupFolder",  # Directory_
     "program",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]Transport.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     'TARGETDIR'  # WkDir
     ),

]

msi_data = {"Shortcut": shortcut_table}

print(base)
setup(name=product_name,
      version="1.0",
      description=product_name,
      options={"build_exe": build_exe_options,
               'bdist_msi': {
                   'data': msi_data,
               }},
      executables=[Executable("main.py", base=base,
                              targetName='Transport.exe',
                              icon='image/app.ico',
                              shortcutName=product_name,
                              shortcutDir=product_name,

                              )
                   ])
