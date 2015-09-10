#!/usr/bin/python2.7
from subprocess import check_output
from time import sleep
import fcntl
from utils import *
import builder
from sys import argv

location="/home/build/CReaMpy_src/"

check_string = "Already up-to-date"
check_fun = lambda a: not check_string in a

git_command = [
		"git",
		"pull"
		]

"""
rm_command = [
		"ssh",
		"jpr4gc@labunix01.cs.virginia.edu",
		"rm",
		"-rf",
		"/home/jpr4gc/public_html/CRM_html/*"
		]

scp_command = [
		"scp",
		"-r",
		"/home/build/CRM_html/",
		"jpr4gc@labunix01.cs.virginia.edu:/home/jpr4gc/public_html"
		]
"""

rm_command = [
        "rm",
        "-rf",
        "/home/build/CRM_latest.tar.gz",
        "/usr/share/nginx/html/CRM"
        ]

package_command = [
        "tar",
        "-C",
        "/home/build/",
        "-czf",
        "/home/build/CRM_latest.tar.gz",
        "CRM_html/"
        ]
scp_command = [
        "cp",
        "-r",
        "/home/build/CRM_html",
        "/usr/share/nginx/html/CRM"
        ]

def main():
	build_stuff()
	if "once" in argv: return
	init()
	run()

def build_stuff():
	builder.build()
	check_output(rm_command)
	check_output(package_command)
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
