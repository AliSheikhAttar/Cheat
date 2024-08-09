# SSH

## on same net
```bash
ssh username@ip
```

## on other net
1. install openssh/openssh-server windows/linux
2. Configure Port Forwarding on the Remote Router
   1. Access the Router’s Admin Panel:
        Use a web browser to go to the router’s IP address (commonly 192.168.1.1 or 192.168.0.1).
   2. Find Port Forwarding Section:
        This might be under settings like "NAT," "Virtual Server," or "Port Forwarding."
   3. Create a Port Forwarding Rule:
        External Port: 22 (or another port if you want to use a non-standard port for security).
        Internal IP: The local IP address of the remote computer.
        Internal Port: 22 (unless you changed the SSH server configuration).
3. Determine the Public IP Address of the Remote Network
4. connect : `ssh username@public_ip_address`



- Ensure its installed
```bash
sudo dpkg -l | grep openssh-server
```

- install
```bash
sudo apt update
sudo apt install openssh-server
```

- ensure it's running
- Systemd-based
```bash
sudo systemctl status ssh
```
- SysVinit-based
```bash
sudo service ssh status
```

- Check firewall rules
```bash
sudo ufw status
```

- allow ssh on firewall
```bash
sudo ufw allow ssh
# for non-standard
sudo ufw allow [your_ssh_port]
```

- Verify SSH Configuration
 /etc/ssh/sshd_config file is correctly set up

- The line `Port 22` should not be commented out or should reflect your custom port.
- The line `PermitRootLogin` no should be set if root login is not required.
- `PasswordAuthentication` yes or no, depending on your security policies.
After making changes to the SSH configuration, restart the SSH service to apply them:
```bash
sudo systemctl restart ssh
```
## Secure the SSH Server
- Use a Non-Standard Port: Change the SSH port from 22 to another number to reduce automated attacks. Modify /etc/ssh/sshd_config on Linux to set a different port and restart the SSH service.
- SSH Key Authentication: Set up SSH keys for passwordless login, which is more secure than password-based authentication.
Disable Root Login: Disable root login via SSH in the SSH server configuration file.
- Use a Firewall: Set up firewall rules to restrict access to only trusted IP addresses if possible.
## Additional Security Considerations
- VPN
- Regularly Update Software
- Monitor SSH Logs
