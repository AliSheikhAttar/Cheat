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

## find a dir/file
```bash
find / -type d/f -name "<challenge>" 2>/dev/null
```

## find file and show the first result
```bash
sudo find / -name 'bpf_jit_enable' -print -quit
```

## redirect the output as argument | kill specific process by name
```bash
pgrep bpftrace | xargs kill -9
``` 

### write to files need permission
```bash
sudo tee <file>
```

## write random to a file
```bash
base64 /dev/urandom | head -c 1M > abigfile.txt
```
> encode binary to ASCCI first 1 megabyte of it 

## suppress error
```bash
command 2>/dev/null
```

## structure of files and dirs
```bash
tree <dir>
```

## find files excluding certain ones
```bash
find -type f -not -name "*.cpp"
```