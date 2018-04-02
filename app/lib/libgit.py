from git import Repo
import subprocess
import os
import shutil

def clone(git_url, repo_dir, use_console_or_gitpython="gitpython", log=True, force=True):
    if force:
        if os.path.exists(repo_dir):
            if log:
                print("--package dir exists, deleting")
            shutil.rmtree(repo_dir)
    else:
        if log:
            print("--not deleting repo_dir")
    if log:
        print("--cloning")
    if use_console_or_gitpython == "console":
        process = subprocess.Popen(["git", "clone", git_url, repo_dir])
        process.wait()
    elif use_console_or_gitpython == "gitpython":
        Repo.clone_from(git_url, repo_dir)
    if log:
        print("--cloning done")
