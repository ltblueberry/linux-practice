import os
import time
import sys

print('fork() practice')

pid = os.fork()

if pid == 0:
    print('[Child] for me fork() returns 0')
    print('[Child] sleep 30')
    time.sleep(30)
    print('[Child] exit')
    sys.exit(0)
else:
    print('[Parent] Child PID: %s' % pid)
    print('[Parent] sleep 10')
    time.sleep(10)
    print('[Parent] exit')
