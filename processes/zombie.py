import os
import time
import sys

print('zombie practice')

pid = os.fork()

if pid == 0:
    print('[Child] Hello')
    for i in range(1, 5):
        time.sleep(1)
    print('[Child] I quit, now I become a zombie')
else:
    print('[Parent] Child PID: %s, I do not look after it' % pid)
    print('[Parent] sleep 60')
    for i in range(1, 60):
        time.sleep(1)
    print('[Parent] exit')
    os.wait()
