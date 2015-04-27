#!/usr/bin/python2.7
from subprocess import check_output
from time import sleep
import fcntl
from utils import *
import builder

location="/home/build/CReaMpy_src/"

check_string = "Already up-to-date"
check_fun = lambda a: not check_string in a

git_command = [
		"git",
		"pull"
		]

def main():
	init()
	run()

def run():
	with open(lock_file, "w") as f:
		while True:
			try:
				fcntl.flock(f, opL_nb)
				print "obtaining lock"
				output = check_output(git_command)
				if check_fun(output, cwd=location):
					print "Going to update now"
					print output
					builder.build()
				else:
					print "no update"
				print "releasing lock"
				fcntl.flock(f, opU)
			except IOError:
				print "unable to acquire lock"
			sleep(seconds(10))

def init():
	#figure out what the number to write is
	pass

if __name__ == "__main__":
	main()
