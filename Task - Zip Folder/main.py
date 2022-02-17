#https://www.guru99.com/python-zip-file.html
#https://stackoverflow.com/questions/2860153/how-do-i-get-the-parent-directory-in-python
#https://docs.python.org/3/library/os.path.html
import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive
from pathlib import Path

#To get the current directory
cwd = os.getcwd()

#Parent path directory
path = Path(cwd)
parent_dir_path = path.parent.absolute()

#Zip complete directory
shutil.make_archive("Parent Directory Zipped", 'zip', parent_dir_path)