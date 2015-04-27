#!/usr/bin/python2.7
import fcntl

lock_file = "update.lock"

seconds = lambda a: a
minutes = lambda a: seconds(a)*60
hours = lambda a: minutes(a)*60

opL_b = fcntl.LOCK_EX
opL_nb = fcntl.LOCK_EX ^ fcntl.LOCK_NB
opU = fcntl.LOCK_UN
