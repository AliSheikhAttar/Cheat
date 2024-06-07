# Cyber

## Why Using the Root User for Logging into a Server is Not Recommended
Using the root user to log into a server is generally not recommended due to several security and operational risks:

Common Knowledge of Root User:

Every hacker knows about the root user. If root login is enabled, hackers are one step closer to executing a brute-force attack.
Full Access and Risk of Errors:

When using the root user, you have full access to perform any action. This increases the likelihood of mistakenly executing harmful commands.
Security Risks with Certain Programs:

Running some programs as the root user poses a security risk because it grants excessive access, which is not desirable.
Difficulty in Tracking Actions:

If your server is accessed by multiple users and they all use the root account, it becomes difficult to determine who executed which command. This makes tracking down a user who performed a malicious action more challenging.

### Create user & add to sudo group & test
```bash
# create user
adduser <new user>
usermod -aG sudo <new user>
# test the root priviliege
su - user
sudo ls /root
# test ssh
ssh <new user>@ip_address_of_server
```
### ban root login to server
```bash
# modify ssh config on server
sudo nano /etc/ssh/sshd_config
# set PermitRootLogin to no

sudo service ssh restart

# run these on server
sudo rm -rf /root/.ssh
sudo passwd --lock root
```
after these following shouldnt be execute
```bash
ssh root@ip_address_of_server
```

### Change default port of ssh

- allow transfer on <port> : random number greater than 1024 (less are preserved)
```bash
sudo ufw allow <port>/tcp
```

- modify ssh config
```bash
sudo nano /etc/ssh/sshd_config
# change the port to new port 
#Port 5522
sudo systemctl restart sshd
```
connect via new port 
```bash
ssh -p <new port> <new user>@remote_host_or_ip
```