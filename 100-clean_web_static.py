#!/usr/bin/python3

# Fabfile for removing outdated  archives.

import os
from fabric.api import *

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_clean(number=0):

    """ Del outdated archives.

    Args:
        number (int): The no of archives to retain.

    If number === 1|0, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.

    """

    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]

    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):

        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        i[run("rm -rf ./{}".format(a)) for a in archives]
