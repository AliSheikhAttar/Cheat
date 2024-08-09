# Network

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

## firewall (Uncomplicated Firewall)
```bash
sudo ufw disable/enable/status/reload
```

- allow transfer on <port> : random number greater than 1024 (less are preserved)
```bash
sudo ufw allow <port>/tcp
```


```bash
sudo systemctl stop/status firewalld
```


- Close a Specific Port
To close a specific port (e.g., port 80), This will block incoming TCP traffic on port 80
```bash
sudo ufw deny 80/tcp
```

- block port for UDP
```bash
sudo ufw deny 80/udp
```

- Close Multiple Ports
You can also close multiple ports at once. For example, to close ports 80 and 443:
```bash
sudo ufw deny 80,443/tcp
```

- Delete a Rule
If you need to remove a rule, you can delete it by specifying the rule:
```bash
sudo ufw delete deny 80/tcp
```

- Reload ufw
ufw automatically applies changes, but if you ever need to reload it manually, you can use:
```bash
sudo ufw reload
```

## ping
```bash
ping google.com
```
- with limitation
```bash
ping google.com -c <n> # n packets
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