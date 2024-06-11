## apt
- package source
```bash
/etc/apt/sources.list
```

- search specific package
```bash
sudo apt search <package>
```

- install
```bash
sudo apt instal <package>
```

- Update installed packages
```bash
sudo apt update
```
- delete package
```bash
sudo apt remove <package>
```
- remove dependencies
```bash
sudo apt autoremove
```

- upgrades the apps, tools, and utilities
```bash
sudo apt-get upgrade
```
-  upgrades the apps, tools, and utilities and installs new Linux kernel of the OS
```bash
sudo apt upgrade
```
- upgrades the apps, tools, and utilities and installs new Linux kernel of the OS. It also removes old packages if needed for the upgrade
```bash
sudo apt full-upgrade
```
- Remove unused packages
```bash
sudo apt full-upgrade
```

## Fix update
- ` sudo apt upgrade -y `
- ` sudo apt update `
- ` sudo apt-get clean ; sudo apt-get check ; sudo apt -f install `
- ` sudo apt-get dist-upgrade -y ; sudo apt-get autoremove -y `

## Fix installination
```bash
sudo apt clean # clearing packages cache
sudo apt update
```

## Mirrors for apt resources
```bash
## mirrors.kernel.org
deb http://mirrors.kernel.org/ubuntu/ focal main restricted
deb http://mirrors.kernel.org/ubuntu/ focal-updates main restricted
deb http://mirrors.kernel.org/ubuntu/ focal universe
deb http://mirrors.kernel.org/ubuntu/ focal-updates universe
deb http://mirrors.kernel.org/ubuntu/ focal multiverse
deb http://mirrors.kernel.org/ubuntu/ focal-updates multiverse
deb http://mirrors.kernel.org/ubuntu/ focal-backports main restricted universe multiverse
deb http://mirrors.kernel.org/ubuntu/ focal-security main restricted
deb http://mirrors.kernel.org/ubuntu/ focal-security universe
deb http://mirrors.kernel.org/ubuntu/ focal-security multiverse
## mirror.cs.uchicago.edu
deb http://mirror.cs.uchicago.edu/ubuntu/ focal main restricted
deb http://mirror.cs.uchicago.edu/ubuntu/ focal-updates main restricted
deb http://mirror.cs.uchicago.edu/ubuntu/ focal universe
deb http://mirror.cs.uchicago.edu/ubuntu/ focal-updates universe
deb http://mirror.cs.uchicago.edu/ubuntu/ focal multiverse
deb http://mirror.cs.uchicago.edu/ubuntu/ focal-updates multiverse
deb http://mirror.cs.uchicago.edu/ubuntu/ focal-backports main restricted universe multiverse
deb http://mirror.cs.uchicago.edu/ubuntu/ focal-security main restricted
deb http://mirror.cs.uchicago.edu/ubuntu/ focal-security universe
deb http://mirror.cs.uchicago.edu/ubuntu/ focal-security multiverse
## ubuntu.mirrors.tds.net
deb http://ubuntu.mirrors.tds.net/ubuntu/ focal main restricted
deb http://ubuntu.mirrors.tds.net/ubuntu/ focal-updates main restricted
deb http://ubuntu.mirrors.tds.net/ubuntu/ focal universe
deb http://ubuntu.mirrors.tds.net/ubuntu/ focal-updates universe
deb http://ubuntu.mirrors.tds.net/ubuntu/ focal multiverse
deb http://ubuntu.mirrors.tds.net/ubuntu/ focal-updates multiverse
deb http://ubuntu.mirrors.tds.net/ubuntu/ focal-backports main restricted universe multiverse
deb http://ubuntu.mirrors.tds.net/ubuntu/ focal-security main restricted
deb http://ubuntu.mirrors.tds.net/ubuntu/ focal-security universe
deb http://ubuntu.mirrors.tds.net/ubuntu/ focal-security multiverse
## ftp.udl.es
deb http://ftp.udl.es/ubuntu/ focal main restricted
deb http://ftp.udl.es/ubuntu/ focal-updates main restricted
deb http://ftp.udl.es/ubuntu/ focal universe
deb http://ftp.udl.es/ubuntu/ focal-updates universe
deb http://ftp.udl.es/ubuntu/ focal multiverse
deb http://ftp.udl.es/ubuntu/ focal-updates multiverse
deb http://ftp.udl.es/ubuntu/ focal-backports main restricted universe multiverse
deb http://ftp.udl.es/ubuntu/ focal-security main restricted
deb http://ftp.udl.es/ubuntu/ focal-security universe
deb http://ftp.udl.es/ubuntu/ focal-security multiverse
```