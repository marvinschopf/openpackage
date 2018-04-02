import os
import pathlib
import shutil
from lib import libgit

def loadList(silent=False):
    directory=".openpackage/packages"
    homedir = str(pathlib.Path.home())
    cloneMethod = "console"
    if silent:
        cloneMethod = "gitpython"
    else:
        cloneMethod = "console"
    if not homedir[-1:] == "/":
        homedir = homedir + "/"
    clonedir = homedir + directory
    if not silent:
        print("--Home directory =", homedir)
        print("--Cloning packages")
        print("--Cloning into", clonedir)
    libgit.clone("https://github.com/openpackage/packages.git", clonedir, log = not silent, use_console_or_gitpython = cloneMethod)
    if not silent:
        print("--Downloaded packages")
