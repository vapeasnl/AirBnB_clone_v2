#!/usr/bin/python3
from fabric.api import put, run, env
from fabric.contrib.files import exists
import os

env.hosts = ['54.162.77.178', '52.87.216.60']

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        print("Error: Archive '{}' does not exist.".format(archive_path))
        return False
    
    try:
        file_name = os.path.basename(archive_path)
        no_ext = os.path.splitext(file_name)[0]
        release_path = "/data/web_static/releases/{}/".format(no_ext)

        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, release_path))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}web_static/* {}'.format(release_path, release_path))
        run('rm -rf {}web_static'.format(release_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_path))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Error deploying:", e)
        return False
