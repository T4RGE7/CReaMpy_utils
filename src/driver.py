#!/usr/bin/python2.7

import time
import os
import signal
import subprocess
import fcntl
import argparse as ap
from ast import literal_eval

from utils import *

p_updater = None
config_file = None
default_config = {
        "time" : 5,
        "u_time" : "m"
        }
config = None

def main():
    global config_file

    parser = ap.ArgumentParser()
    parser.add_argument("config", help="the file to work on")
    args = parser.parse_args()

    config_file = args.config

    try:
        verify_config()
    except:
        print "ERROR: config file is wrong"
        exit(1)

    cmd = ["./updater.py"]
    p_updater = subprocess.Popen(cmd)

def run():
    while True:
        print "here"
        time.sleep(seconds(5))

def verify_config():
    if os.path.isfile(config_file):
        with open(config_file, "r") as f:
            tmp = "".join(f.readlines())
            tmp_eval = literal_eval(tmp)
            if type(tmp_eval) is dict:
                return tmp_eval
    raise

def update_config():
    global config
    with open(lock_file, "w") as f:
        try:
            fcntl.flock(f, opL_b)
            tmp = verify_config()
            
            pass
        except IOError:
            config = dict(default_config)
        except:
            print "ERROR: something moved the file"

if __name__ == "__main__":
    main()
