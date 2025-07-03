import os
from shutil import rmtree, copy

def recursive_copy_files(src, dest):
    if os.path.exists(dest):
        rmtree(dest)
    os.mkdir(dest)
    for path in os.listdir(src):
        srcpath = os.path.join(src, path)
        if os.path.isfile(srcpath):
            copy(srcpath, dest)
        else:
            recursive_copy_files(srcpath, os.path.join(dest, path))