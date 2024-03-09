#!/usr/bin/python3
"""
Del out-of-date arch.
"""

import os
from fabric.api import *

env.hosts = ['100.26.243.2', '54.160.99.137']


def do_clean(number=0):
    """Delete out-of-date arch. """
    number = 1 if int(number) == 0 else int(number)

    arch = sorted(os.listdir("versions"))
    [arch.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in arch]

    with cd("/data/web_static/releases"):
        arch = run("ls -tr").split()
        arch = [a for a in arch if "web_static_" in a]
        [arch.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in arch]
