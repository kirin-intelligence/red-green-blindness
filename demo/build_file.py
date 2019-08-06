import os
import shutil


# shutil.rmtree("C:/Users/tsq/Desktop/work/red-green-blindness/demo/build/bdist.win32")

# C:/Users/tsq/Desktop/work/red-green-blindness/demo/build_file.py
# bdist_msi
# os.system('C:/Users/tsq/AppData/Local/Programs/Python/Python36-32/python.exe setup.py clean')
# os.system('C:/Users/tsq/AppData/Local/Programs/Python/Python36-32/python.exe setup.py bdist_msi')
# shutil.rmtree("C:/Users/tsq/Desktop/work/red-green-blindness/demo/build/bdist.win-amd64")
# os.system('C:/Users/tsq/AppData/Local/Programs/Python/Python36/python.exe setup.py bdist_msi')

def build_64():
    shutil.rmtree("C:/Users/tsq/Desktop/work/red-green-blindness/demo/build/bdist.win-amd64")
    shutil.rmtree("C:/Users/tsq/Desktop/work/red-green-blindness/demo/dist")

    shutil.rmtree("C:/Users/tsq/Desktop/work/red-green-blindness/demo/build/exe.win-amd64-3.6")
    # os.system('C:/Users/tsq/AppData/Local/Programs/Python/Python36/python.exe setup.py bdist_msi')


if __name__ == '__main__':
    import sys

    if sys.argv[1] == '6':
        build_64()
