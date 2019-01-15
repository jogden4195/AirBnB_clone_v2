#!/usr/bin/python3
from fabric.api import *
from fabric.contrib import files
import datetime
import ntpath

env.user = 'ubuntu'
env.hosts = ['35.229.84.121', '34.73.176.33']


def deploy():
    """
    deploy - creates and distributes an archive to your servers
    Return: True if success, False if failure
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


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
    mkdir = run(command)
    if mkdir.failed:
        return False
    command = "sudo tar -zxf /tmp/" + filename + " -C " + target
    uncompress = run(command)
    if uncompress.failed:
        return False

    # Remove archive file and delete sym link /data/web_static/current
    command = 'sudo rm /tmp/' + filename
    run(command)
    command = 'sudo mv ' + target + '/web_static/* ' + target
    run(command)
    command = 'sudo rm -rf ' + target + '/web_static'
    run(command)

    # Creating new sym link
    command = 'sudo ln -sfn ' + target + ' /data/web_static/current'
    link = run(command)
    if link.failed:
        return False

    print("New version deployed!")
    return True


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
    path = "./versions/" + archive_name
    return path
