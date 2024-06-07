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

- which ports are used
```bash
lsof -i:<port> 
```
- kill ssh
```bash
killall ssh
```

- firewall (Uncomplicated Firewall)
```bash
sudo ufw disable/enable/status
```

- allow transfer on <port> : random number greater than 1024 (less are preserved)
```bash
sudo ufw allow <port>/tcp
```


```bash
- sudo systemctl stop/status firewalld
```

## proxy
- Reset proxy
```bash
unset http_proxy
unset https_proxy
unset HTTP_PROXY
unset https_proxy
unset HTTPS_PROXY
unset all_proxy
unset ALL_PROXYz
```
- clear proxy
```bash
export http_proxy=""
export https_proxy=""
export HTTP_PROXY=""
export HTTPS_PROXY=""
export all_proxy=""
export ALL_PROXY=""

```
- view proxy
```bash
echo $http_proxy
echo $https_proxy
```

- ARP cache table
```bash
 arp - a
```

- add entry to ARP cache table statically
```bash
 arp -s <ip address> <mac address>
```