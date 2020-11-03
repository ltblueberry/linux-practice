# processes

## fork()

Create fork() in python programm, check PID, check prcesses status

![fork](screenshots/screenshot-fork.png)
![ps aux](screenshots/screenshot-psaux.png)

## zombie

Parent process do not handle exit of child process, child become a zombie

![zombie](screenshots/screenshot-zombie.png)
![zombie ps aux](screenshots/screenshot-zombie-psaux.png)


## stop

Process receive SIGSTOP, and then wait for SIGKILL or SIGCONT.

![stop](screenshots/screenshot-stop.png)
![cont](screenshots/screenshot-stop-cont.png)


## pstree

```
sudo yum install psmisc

pstree
```
![pstree](screenshots/screenshot-pstree.png)