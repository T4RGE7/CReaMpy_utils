#!/usr/bin/python2.7
import pyinotify
from time import sleep

"""
wm = pyinotify.WatchManager()
mask = pyinotify.ALL_EVENTS

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
excl = lambda a: ".git" in a
wdd = wm.add_watch('/home/user/Documents/repos/CReaMpy_utils/test', mask, rec=True, auto_add=True, exclude_filter=excl)
notifier.loop()
"""

def excfun(ignore):
    def toRet(s):
        #print s
        return reduce(lambda a,c: a or (c in s), ignore, False)
    return toRet

f = excfun(set([".swp", ".swx", "4913"]))

class EventHandler(pyinotify.ProcessEvent):
    def process_default(self, event):
        return
        if f(str(event.pathname)): return
        print "%s:\n\t%s" % (event.maskname, str(event.pathname))

    def process_IN_MODIFY(self, event):
        if f(str(event.pathname)): return
        print "%s:\n\t%s" % (event.maskname, str(event.pathname))
        sleep(10)



class Watcher():
    def __init__(self):
        pass

    def run(self):
        self.wm = pyinotify.WatchManager()
        self.handler = EventHandler()
        #self.mask = pyinotify.ALL_EVENTS ^ (pyinotify.IN_ISDIR|pyinotify.IN_CLOSE_NOWRITE|pyinotify.IN_OPEN|pyinotify.IN_ACCESS|pyinotify.IN_ATTRIB)
        self.mask = pyinotify.IN_MODIFY
        self.notifier = pyinotify.AsyncNotifier(self.wm, self.handler)
        self.ignore = set([".git"])
        self.exclusionFun = lambda path: reduce(lambda a,c: a or (c in path), self.ignore, False)
        self.exclusionFun = excfun(self.ignore)
        self.watchpath = '/home/user/Documents/repos/CReaMpy_utils/test'
        self.wdd = self.wm.add_watch(self.watchpath, self.mask, rec=True, auto_add=True, exclude_filter=self.exclusionFun)
        self.notifier.loop()

def main():
    watch = Watcher()
    watch.run()

if __name__ == "__main__":
    main()
