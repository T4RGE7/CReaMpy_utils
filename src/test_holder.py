import fcntl
from time import sleep
opL = fcntl.LOCK_EX ^ fcntl.LOCK_NB
opU = fcntl.LOCK_UN
f2 = open("update.lock", "w")
fcntl.flock(f2, opL)
sleep(20)
fcntl.flock(f2, opU)

