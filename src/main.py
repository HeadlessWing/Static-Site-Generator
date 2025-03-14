from textnode import *
from htmlnode import *
import os
import shutil

def copy_static_to_public():
    if os.path.exists("./static") == False: # or 
        raise Exception("required paths do not exist")
    if os.path.exists("./public") == True:
        shutil.rmtree("./public")
    os.mkdir("./public")
    copy_dir("./static", "./public" )

def copy_dir(origin, destination):
    files = os.listdir(origin)
    for file in files:

        n_origin = os.path.join(origin, file)
        if os.path.isfile(n_origin) == True:
            shutil.copy(n_origin, destination)
        if os.path.isdir(n_origin) == True:
            n_destination = os.path.join(destination, file)
            os.mkdir(n_destination)
            copy_dir(n_origin, n_destination)


def main():
    copy_static_to_public()
    



main()