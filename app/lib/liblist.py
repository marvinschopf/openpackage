import os
import pathlib
import shutil
from lib import libgit

def loadList():
    directory=".openpackage/packages"
    homedir = str(pathlib.Path.home())
    if not homedir[-1:] == "/":
        homedir = homedir + "/"
    clonedir = homedir + directory
    print("--Home directory =", homedir)
    print("--Cloning packages")
    print("--Cloning into", clonedir)
    libgit.clone("https://github.com/openpackage/packages.git", clonedir)
    print("--Downloaded packages")
