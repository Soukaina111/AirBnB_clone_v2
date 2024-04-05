#!/usr/bin/python3
# This script uses  fabfile to distribute an archive to a web server.

from fabric.api import env
from fabric.api import put
from fabric.api import run
import os.path

env.hosts = ["52.87.254.240", "54.237.1.11"]


def do_deploy(archive_path):
    '''distributes an archive to your web servers
    using the function do_deploy'''
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    call = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
            format(call)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
            format(call)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(file, call)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(call, call)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(call)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(call)).failed is True:
        return False
    return True
