# Linux Network

- reset network and proxy settings
1.  
```bash
sudo nano /etc/resolv.conf
```
2. type _nameserver 8.8.8.8 nameserver 8.8.4.4_ and Exit
axel -a -n [Num_of_Thread] link1 link2 link3 ...

- reset DNS
1. sudo nano /etc/network/interfaces
2. type dns-nameservers 8.8.8.8
- Download with multiple threads
```bash
axel -a -n [Num_of_Thread] link1 link2 link3 ...
```

- firewall
```bash
sudo ufw disable/enable/status
```


```bash
- sudo systemctl stop/status firewalld
```

- Reset proxy
```bash
unset http_proxy https_proxy
```
