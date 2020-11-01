# strace

# Build
```
gcc -g printf.c -o printf
```

# Trace
C program
```
strace -o printf.log ./printf
```

C program ltrace
```
ltrace -o printf-ltrace.log ./printf
```

Python program
```
strace -o print.log python ./print.py 
```

NodeJS program
```
strace -o consolelog.log node ./consolelog.js
```

By PID
```
strace -p <pid>
```

# Filtering
```
strace -e trace=network <command>
```

Available:
* file
* process
* network
* signal
* memory
* ...

```
strace -e trace=file ./printf

execve("./printf", ["./printf"], 0x7ffe1ea1d270 /* 26 vars */) = 0
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
open("/lib64/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
practice string
+++ exited with 0 +++
```

```
strace -e trace=process ./printf

execve("./printf", ["./printf"], 0x7ffdd5857680 /* 26 vars */) = 0
arch_prctl(ARCH_SET_FS, 0x7f44e4996740) = 0
practice string
exit_group(0)                           = ?
+++ exited with 0 +++
```

```
strace -e read,write ./printf

read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0`&\2\0\0\0\0\0"..., 832) = 832
write(1, "practice string\n", 16practice string
)       = 16
+++ exited with 0 +++
```


# Inspect
```
grep write <logfile>
```

