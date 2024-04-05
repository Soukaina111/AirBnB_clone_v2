#!/usr/bin/python3
# This fabfile to create and distribute an archive to web servers.

import os
from datetime import datetime
from fabric.api import env, local, put, run

env.hosts = ['52.87.254.240', '54.237.1.11']


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file_name = f"versions/web_static_{dt.strftime('%Y%m%d%H%M%S')}.tgz"
    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    if local(f"tar -cvzf {file_name} web_static").failed:
        return None
    return file_name


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
    current_path = "/data/web_static/current"

    if put(archive_path, tmp_path).failed:
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


def deploy():
    """Deploy the web static files to the web servers."""
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)


if __name__ == "__main__":
    deploy()
