#!/usr/bin/python3
# This script uses  fabfile to distribute an archive to a web server.
import os
from fabric.api import env, put, run

env.hosts = ["52.87.254.240", "54.237.1.11"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.isfile(archive_path):
        return False
    
    file_name = archive_path.split("/")[-1]
    name = file_name.split(".")[0]
    tmp_path = f"/tmp/{file_name}"
    release_path = f"/data/web_static/releases/{name}/"
        return False
    if run(f"rm -rf {release_path}").failed:
        return False
    if run(f"mkdir -p {release_path}").failed:
        return False
    if run(f"tar -xzf {tmp_path} -C {release_path}").failed:
        return False
    if run(f"rm {tmp_path}").failed:
        return False
    if run(f"mv {release_path}web_static/* {release_path}").failed:
        return False

    if run(f"rm -rf {release_path}web_static").failed:
        return False

    if run(f"rm -rf {current_path}").failed:
        return False

    if run(f"ln -s {release_path} {current_path}").failed:
        return False

    return True

