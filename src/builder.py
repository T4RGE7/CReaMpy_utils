#!/usr/bin/python2.7
import re
from os.path import isfile
from subprocess import call
import header 

wiki_location="/home/build/CReaMpy_src/"
header_location="/home/build/CRM/"
link_format="[[%s|%s]]"

contents = [
		'=== Contents ==='
		]

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

def remake(tree_list, depth):
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

                        if current == "Contents":
                            lines = contents + make_contents(depth)
                        else:
                            lines += get_subcontents(current, depth)

			lines = [header+"\n"] + lines + ["\n"+header]

			with open(header_location + current + ".wiki", "w") as out:
				out.writelines(lines)
	#print " ".join(recompile_args)
	call(recompile_args)

def make_contents(depths):
	toReturn = []

	for name, td in depths:
		toReturn += ["%s* [[%s]]" % ("\t"*(td), name)]

	return toReturn

def build():
	tree = header.read_file()
	header_list = header.parse(tree)
	depth = header.get_depth(tree)

	remake(header_list, depth)


def get_subcontents(node, depths):

    start = map(lambda (n,d): n, depths).index(node)
    end = start + 1
    for n,d in depths[start+1:]:
        if d <= depths[start][1]:
            break
        end += 1

    if start + 1 == end:
            return []

    start_depth = depths[start+1][1]

    content_list = make_contents(map(lambda (n,d): (n,d-start_depth), depths[start+1:end]))

    return map(lambda a: a+"\n", content_list)


	
def main():

	tree = header.read_file()
	header_list = header.parse(tree)
	depth = header.get_depth(tree)
        print depth
	contents_lines = contents + make_contents(depth)

        for e in contents_lines:
            pass
            print e

	"""
	for cur,prev,up,nex in header_list:
		print str(cur) + "\t" + str(up)
	"""

	#remake(header_list)
	"""
        for cur, dnc, dnnc, dnnnc in header_list:
		with open("/home/user/Documents/school/notes/" + cur + ".wiki", "r") as r:
			with open("/home/user/Documents/repos/CReaMpy_src/CRM/" + cur + ".wiki", "w") as w:
				w.writelines(r.readlines())
	"""


if __name__ == "__main__":
	main()
