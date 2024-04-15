# Linux Network

- reset network and proxy settings
1.  
```bash
sudo nano /etc/resolv.conf
```
2. type _nameserver 8.8.8.8_ and Exit
axel -a -n [Num_of_Thread] link1 link2 link3 ...

- Download with multiple threads
```bash
axel -a -n [Num_of_Thread] link1 link2 link3 ...
```

- firewall
```bash
sudo ufw disable/enable/status
```

- sudo systemctl stop/status firewalld