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

# Inspect
```
grep write <logfile>
```

