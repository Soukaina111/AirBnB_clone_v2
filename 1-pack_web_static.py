#!/usr/bin/python3
# This script uses  Fabfile to generate a
# tgz archive from the contents of web_static.
import os
from datetime import datetime
from fabric.api import local


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
