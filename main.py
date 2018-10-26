from threading import Thread
import hook
import sv
import time

def runA():
    hook.init_hook()

#def runB():
#    sv.init_host()

t1 = Thread(target = runA)
#t2 = Thread(target = runB)
t1.setDaemon(True)
#t2.setDaemon(True)
t1.start()
#t2.start()
while 1:
    events = hook.get_events()
    if events:
        sv.send_events(events)
    pass