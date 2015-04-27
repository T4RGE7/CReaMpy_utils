#!/usr/bin/python2.7
import re
from os.path import isfile
from subprocess import call
import header 

wiki_location="/home/build/CReaMpy_src/"
header_location="/home/build/CRM/"
link_format="[[%s|%s]]"

recompile_args = [
		'bash',
		'build.sh'
		]

replace_list = [
		("[.]", ""),
		("[,]", ""),
		("[ ]", "")
		]

link_list = [
		
		]

def remove(s):
	return reduce(lambda a, (rep,wit): re.sub(rep,wit,a), replace_list, s)

def remake(tree_list):
	for current, prev_s, up_s, next_s in tree_list:
		to_open = wiki_location + "CRM/" + current + ".wiki"
		if not isfile(to_open):
			print "Need to make " + to_open
			continue
		with open(to_open, "r") as f:
			lines = f.readlines()
			#up, prev, nex = map(remove, [up_s,prev_s,next_s])
			up, prev, nex = up_s, prev_s, next_s
			p = "" if prev is None else link_format%(prev,"Previous")
			u = "" if up is None else link_format%(up,"Up")
			n = "" if nex is None else link_format%(nex,"Next")

			header = "%s %s %s" % (p, u, n)

			lines = [header+"\n"] + lines + ["\n"+header]

			with open(header_location + current + ".wiki", "w") as out:
				out.writelines(lines)
	#print " ".join(recompile_args)
	call(recompile_args)

def build():
	tree = header.read_file()
	header_list = header.parse(tree)
	remake(header_list)

	
def main():

	tree = header.read_file()
	header_list = header.parse(tree)

	"""
	for cur,prev,up,nex in header_list:
		print str(cur) + "\t" + str(up)
	"""

	remake(header_list)


if __name__ == "__main__":
	main()
