# CMDZ
## sort all processes by start time
```bash
ps -eo pid,lstart,cmd --sort=-lstart
```

## sort all processes by CPU usage then memory usage.
```bash
ps -eo pid,pcpu,pmem,cmd --sort=-pcpu,-pmem
```

## kill the output of ps
```bash
ps -ef | grep <'/snap/pycharm-community'> | grep -v grep | awk '{print $2}' | xargs kill
```

## Update specific package
```bash
sudo apt upgrade telegram-desktop
```

## find file and show the first result
```bash
sudo find / -name 'bpf_jit_enable' -print -quit
```