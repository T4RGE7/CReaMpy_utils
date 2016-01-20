#!/usr/bin/python2.7
import fcntl
import os
import datetime
"""
from db import DB

lock_file = "update.lock"
log_db = "crm.db"
log_schema_create = "log(id INTEGER PRIMARY KEY, time STRING, sev INTEGER, message STRING)"
log_insert = "INSERT INTO log (time,  sev, message) VALUES (?,?,?)"
"""

seconds = lambda a: a
minutes = lambda a: seconds(a)*60
hours = lambda a: minutes(a)*60

opL_b = fcntl.LOCK_EX
opL_nb = fcntl.LOCK_EX ^ fcntl.LOCK_NB
opU = fcntl.LOCK_UN

modification_date = lambda filename: datetime.datetime.fromtimestamp(os.path.getmtime(filename))

now = lambda: datetime.datetime.utcnow().isoformat()
"""
getLogMessage = lambda sev, msg: [now(), sev, msg]
logDB = DB().connect(log_db, log_schema_create)

def logMessage(sev, msg):
    logDB.execute(log_insert, getLogMessage(sev, msg))
    DB().commit(log_db)
"""
