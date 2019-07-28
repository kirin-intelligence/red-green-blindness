import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_exe_options = {
    "include_files": ["lib", 'image', 'python36.dll'],
    "packages": ["pyqt5", "os", "sys","xlwings","numpy"], "excludes": []}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "win32gui"
base = None

# product_name = u'交通拥堵分析系统'.encode('gb2312')
# exec_name = u'交通拥堵分析系统.exe'.encode('gb2312')
product_name = 'Transport'
exec_name = 'Transport'
print(base)
setup(name=product_name,
      version="1.0",
      description=product_name,
      options={"build_exe": build_exe_options,
               },
      executables=[Executable("main.py", base=base,
                              targetName='Transport.exe',
                              icon='image/app.ico',

                              )
                   ])
