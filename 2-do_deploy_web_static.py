#!/usr/bin/python3
from fabric.api import *
from fabric.contrib import files
import datetime
import ntpath


env.user = 'ubuntu'
env.hosts = ['35.229.84.121', '34.73.176.33']


def do_deploy(archive_path):
    """
    do_deploy - distributes an archive to your web servers
    Return: True if all operations were successful, False if error
    """
    # Check if archive_path exists
    if archive_path is None:
        return False

    # Uploading archive to the /tmp/
    put(archive_path, "/tmp/")
    filename = ntpath.basename(archive_path)

    # Creating dir to put archive files & uncompressing them there
    target = "/data/web_static/releases/" + filename[:-4]
    command = "mkdir -p " + target
    run(command)
    command = "sudo tar -zxf /tmp/" + filename + " -C " + target
    run(command)

    # Remove archive file and delete sym link /data/web_static/current
    command = 'sudo rm /tmp/' + filename
    run(command)
    command = 'sudo mv ' + target + '/web_static/* ' + target
    run(command)
    command = 'sudo rm -rf ' + target + '/web_static'
    run(command)
    command = 'sudo rm -rf /data/web_static/current'
    run(command)

    # Creating new sym link
    command = 'sudo ln -sfn ' + target + ' /data/web_static/current'
    run(command)

    return True
