""" Module for network specific helper functions """
import os
import subprocess
import platform

def ping(host):
    """ Returns true if host responds to a ping request """
    ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    with open(os.devnull, 'wb') as devnull:
        return subprocess.call(["ping", ping_str, host],
                               stdout=devnull, stderr=devnull) == 0
