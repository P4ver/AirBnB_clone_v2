#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

from fabric.api import env, put, run
from os.path import exists

env.hosts = ['100.26.243.2', '54.160.99.137']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        archive_base = archive_name.split('.')[0]
        remote_path = '/data/web_static/releases/'

        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(remote_path, archive_base))
        run('tar -xzf /tmp/{} -C {}{}/'.format(
            archive_name, remote_path, archive_base))

        run('rm /tmp/{}'.format(archive_name))

        run('rm -rf /data/web_static/current')

        run('ln -s {}{}/ /data/web_static/current'.format(
            remote_path, archive_base))

        print("New version deployed!")
        return True
    except Exception:
        return False
