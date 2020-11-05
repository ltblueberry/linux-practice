# la

## CPU usage
To produce high CPU load for 1 cpu
```
stress --cpu 1 --timeout 600
```

Check **top**

![ps](screenshots/screenshot-cpu-top.png)

Check **/proc/loadavg**

![ps](screenshots/screenshot-cpu-loadavg.png)
The value for 1m avarage is growing, but there are only 2-4 active process with 125 total processes

Check **vmstat** every 1 second

![ps](screenshots/screenshot-cpu-vmstat-100.png)
These are percentages of total CPU time. 
**CPU us** - Time spent running non-kernel code. Our **stress** command use all CPU time.

Stop **stress** process, check **vmstat** again

![ps](screenshots/screenshot-cpu-vmstat-0.png)
No more **CPU us** load