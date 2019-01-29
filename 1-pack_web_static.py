#!/usr/bin/python3
from fabric.api import *
from fabric.contrib import files
import datetime


def do_pack():
    """
    do_pack - generates a .tgz archive from the contents
    of the web_static folder of our AirBnB Clone repo
    Return: Archive path if success, None if failure
    """
    time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_" + time + ".tgz"
    command = "tar -cvzf " + archive_name + " ./web_static/"
    local(command)
    local("mkdir -p versions")
    command = "mv " + archive_name + " ./versions/"
    local(command)
    command = "readlink -f " + archive_name
    path = local(command)
    print("PATH: ", path)
    return path
