#!/usr/bin/python3
''' # This fabfile to create and distribute an archive to web servers '''
import os
from datetime import datetime
from invoke import Context

# Define a connection context for each host
contexts = [Context(host=host) for host in ['52.87.254.240', '54.237.1.11']]

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file_name = f"versions/web_static_{dt.strftime('%Y%m%d%H%M%S')}.tgz"
    
    if not os.path.isdir("versions"):
        if Context().run("mkdir -p versions").failed:
            return None
    
    if Context().run(f"tar -cvzf {file_name} web_static").failed:
        return None
    
    return file_name

def do_deploy(archive_path):
    """Distributes an archive to a web server."""
    if not os.path.isfile(archive_path):
        return False
    
    file_name = archive_path.split("/")[-1]
    name = file_name.split(".")[0]
    tmp_path = f"/tmp/{file_name}"
    release_path = f"/data/web_static/releases/{name}/"
    current_path = "/data/web_static/current"

    # Upload the archive to the server
    for ctx in contexts:
        if ctx.put(archive_path, tmp_path).failed:
            return False

        # Remove the existing release directory
        if ctx.run(f"rm -rf {release_path}").failed:
            return False

        # Create a new release directory
        if ctx.run(f"mkdir -p {release_path}").failed:
            return False

        # Extract the archive to the new release directory
        if ctx.run(f"tar -xzf {tmp_path} -C {release_path}").failed:
            return False

        # Remove the uploaded archive
        if ctx.run(f"rm {tmp_path}").failed:
            return False

        # Move the contents of the web_static directory to the release directory
        if ctx.run(f"mv {release_path}web_static/* {release_path}").failed:
            return False

        # Remove the now-empty web_static directory
        if ctx.run(f"rm -rf {release_path}web_static").failed:
            return False

        # Remove the current symlink
        if ctx.run(f"rm -rf {current_path}").failed:
            return False

        # Create a new symlink to the new release
        if ctx.run(f"ln -s {release_path} {current_path}").failed:
            return False

    return True

def deploy():
    """Deploy the web static files to the web servers."""
    # Create the archive
    archive_path = do_pack()
    if archive_path is None:
        return False

    # Deploy the archive to the web servers
    return do_deploy(archive_path)

# Execute the deploy function
if __name__ == "__main__":
    deploy()

