#!/usr/bin/python3
"""
fabric scrpt to distribute an arch to web server.
"""
from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.160.99.137', '100.26.243.2']


def do_deploy(archPth):
    """distributes an arch to web srvr"""
	if not exists(archPth):
        return False
    try:
        fleN = archPth.split("/")[-1]
        nExt = fleN.split(".")[0]
        pth = "/data/web_static/releases/"
        put(archPth, '/tmp/')
        run('mkdir -p {}{}/'.format(pth, nExt))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fleN, pth, nExt))
        run('rm /tmp/{}'.format(fleN))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(pth, nExt))
        run('rm -rf {}{}/web_static'.format(pth, nExt))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(pth, nExt))
        return True
    except:
        return False
