import os
import time
import sys
import signal

print('signal practice')


def sigchld_handler(signal_number, stack_frame):
    print("[SIGCHLD] I've got signal %s" % signal_number)
    print('[SIGCHLD] Complete child process')
    os.wait()


signal.signal(signal.SIGCHLD, sigchld_handler)

pid = os.fork()

if pid == 0:
    print('[Child] Hello')
    for i in range(1, 5):
        time.sleep(1)
    print('[Child] I quit, now I will try to become a zombie')
    sys.exit(0)
else:
    print('[Parent] Child PID: %s, and I am looking after it' % pid)
    print('[Parent] sleep 60')
    for i in range(1, 60):
        time.sleep(1)
    print('[Parent] exit')
