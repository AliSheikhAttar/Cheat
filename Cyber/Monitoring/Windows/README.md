# Windows

- pid who created sessions by our system
```shell
netstate -o
```

- users(ip) connected to file shares on our system
```shell
net session
```

- running processes
```shell
tasklist
```

- kill process
```shell
taskkill /IM <image#notepad.exe> /F # with /F not saving any data from image
```

- current logged in user
```shell
whoami
# for logonid
whoami /logonid
```

- statistics of system
info such as # sessions accepted, # password violations, # permission violation 
```shell
net statistics server
```

- list of user accounts on system
```shell
net user
```

- list of groups on system
```shell
net localgroup
```

- list of shared resources and location on the disk on system
```shell
net share
```

