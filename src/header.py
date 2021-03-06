from ast import literal_eval
from config import *

locs = get_updated_locs(None)
#location="/home/user/Documents/repos/CReaMpy_src/"
def read_file():
    structure = literal_eval("".join(open(join_list(locs, [src_git, tree_file]), "r").readlines()))
    return structure

def parse(tree):
    toReturn = []
    todo = [(tree[:],0)]
    old_depth = 0

    up = None
    previous_file = None
    next_file = None

    stack = [None]

    while len(todo) > 0:
        current,depth = todo.pop(0)
        name = current[0]

        if previous_file is not None:
            toReturn[-1][3] = name

        if old_depth > depth:
            up = stack[depth-old_depth-1]
            #print up + "\t"*3 + str(stack)
            stack = stack[:depth-old_depth]
            #print "\t"*3 + str(stack)
        old_depth = depth

        toReturn += [[name, previous_file, up, next_file]]
        previous_file = name

        if len(current) == 1:
            # just a leaf
            pass
        else:
            # parent
            up = name
            stack += [name]
            todo = map(lambda a: (a,depth+1), current[1]) + todo
            pass
    toReturn[-1][3] = None

    return toReturn

def get_depth(tree):
    toReturn = []
    todo = [(tree[:],0)]
    old_depth = 0

    up = None
    stack = [None]

    while len(todo) > 0:
        current,depth = todo.pop(0)
        name = current[0]

        if old_depth > depth:
            up = stack[depth-old_depth-1]
            stack = stack[:depth-old_depth]
        old_depth = depth

        toReturn += [(name, depth)]

        if len(current) != 1:
            stack += [name]
            todo = map(lambda a: (a,depth+1), current[1]) + todo

    return toReturn

def main():
    tree = read_file()
    parse(tree)


if __name__ == "__main__":
    main()
