"""
log.py
Created 11/13/19 by CodeLongAndProsper90
Requires:
    data.py: settings
    time: ctime, time
"""
def log(msg):
    from data import settings
    from time import ctime, time
    if settings['debug'] == True:
        log = open('.genisislog', 'a')
        log.write(str(ctime(time())) + ' : ' + msg + '\n')
        log.close()
