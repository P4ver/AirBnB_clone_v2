#!/usr/bin/python3
"""
Fabric script to generate a tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """
    making an archive on web_static folder
    """

    tm = datetime.now()
    arch = 'web_static_' + tm.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    crt = local('tar -cvzf versions/{} web_static'.format(arch))
    if crt is not None:
        return arch
    else:
        return None
