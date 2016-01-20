#!/usr/bin/python2.7
from subprocess import check_output
from time import sleep
import fcntl
from utils import *
import builder
from sys import argv
import config as c

locs = c.get_updated_locs(None)
html_loc = c.join_list(locs, [c.output_folder, c.html_folder])
html_folder = locs[c.html_folder]
tar_loc = c.join_list(locs, [c.output_folder, c.tar_file])
tar_dir = c.join_list(locs, [c.output_folder, c.html_folder])

location=locs[c.src_git]

check_string = "Already up-to-date"
check_fun = lambda a: not check_string in a

git_command = [
        "git",
        "pull"
        ]

rm_command = [
        "rm",
        "-rf",
        tar_loc,
        html_loc
        ]
rm_command2 = [
        "rm",
        "-rf",
        "/usr/share/nginx/html/CRM",
        ]

package_command = [
        "tar",
        "-C",
        tar_dir,
        "-czf",
        tar_loc,
        "./"
        ]

print " ".join(package_command)

scp_command = [
        "cp",
        "-r",
        html_loc,
        "/usr/share/nginx/html/CRM"
        ]

def main():
    build_stuff()
    if "once" in argv or "onlypackage" in argv: return
    init()
    run()

def build_stuff():
    if "onlypackage" in argv:
        builder.build()
        check_output(package_command)
    else:
        check_output(rm_command)
        builder.build()
        check_output(package_command)
        check_output(rm_command2)
        check_output(scp_command)


def run():
    with open(lock_file, "w") as f:
        while True:
            sleep(minutes(5))
            try:
                fcntl.flock(f, opL_nb)
                print "obtaining lock"
                output = check_output(git_command, cwd=location)
                if check_fun(output):
                    print "Going to update now"
                    #print output
                    build_stuff()
                else:
                    print "no update"
                print "releasing lock"
                fcntl.flock(f, opU)
            except IOError:
                print "unable to acquire lock"

def init():
    #figure out what the number to write is
    pass

if __name__ == "__main__":
    main()
