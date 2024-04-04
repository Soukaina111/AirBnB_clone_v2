#!/usr/bin/python3
""" This script answers this: Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers
using the function do_deploy
"""
from fabric.api import *
from fabric.operations import put
from datetime import datetime
import os

env.hosts = ["52.87.254.240", "54.237.1.11"]


def do_pack():
    """ This function packages all thefile coming from web-static to tgz
    """
    n = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    outc = local('tar -cvf versions/web_static_{}.tgz web_static'
                   .format(n))
    if outc.failed:
        return None
    else:
        return outc


def do_deploy(archive_path):
    """ This function deploys a backup file web_01 and web_02"""

    if not os.path.isfile(archive_path):
        print('archive file does not exist...')
        return False
    try:
        backup = archive_path.split('/')[1]
        no_archive_ext = backup.split('.')[0]
    except Exception:
        print('failed to get archive name from split...')
        return False
    file2 = put(archive_path, '/tmp/')
    if file2.failed:
        return False
    nex = run('mkdir -p /data/web_static/releases/{}/'.format(no_archive_ext))
    if nex.failed:
        print('failed to create archive directory for relase...')
        return False
    nex = run('tar -C /data/web_static/releases/{} -xzf /tmp/{}'.format(
               no_archive_ext, archive))
    if nex.failed:
        print('failed to untar archive...')
        return False
    nex = run('rm /tmp/{}'.format(archive))
    if nex.failed:
        print('failed to remove archive...')
        return False
    nex = run('mv /data/web_static/releases/{}/web_static/* \
               /data/web_static/releases/{}'
              .format(no_archive_ext, no_archive_ext))
    if nex.failed:
        print('failed to move extraction to proper directory...')
        return False
   nex = run('rm -rf /data/web_static/releases/{}/web_static'
              .format(no_archive_ext))
    if nex.failed:
        print('failed to remove first copy of extraction after move...')
        return False
    nex = run('rm -rf /data/web_static/current')
    if nex.failed:
        print('failed to clean up old release...')
        return False
    nex = run('ln -sfn /data/web_static/releases/{} /data/web_static/current'
              .format(no_archive_ext))
    if nex.failed:
        print('failed to create link to new release...')
        return False

    print('\n Congrats! A new Version is now available!\n')

    return True
