## apt
- package source
```bash
/etc/apt/sources.list
```

- search specific package
```bash
sudo apt search <package>
```
- installed packages
```bash
sudo dpkg -l | grep openssh-server
```

- install
```bash
sudo apt install <package>
```

- Update installed packages
```bash
sudo apt update
```
- delete package
```bash
sudo apt remove <package>
sudo apt-get purge <package>
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
```bash
sudo apt upgrade -y
sudo apt update 
sudo apt-get clean ; sudo apt-get check ; sudo apt -f install 
sudo apt-get dist-upgrade -y ; sudo apt-get autoremove -y 
```
## Fix installination
```bash
sudo apt clean # clearing packages cache
```

# Repository
In Ubuntu and other Debian-based systems, repositories are collections of software packages that you can install on your system using a package manager like apt. Different repositories serve different purposes. Here’s a quick breakdown of the key repositories:

1. Main Repository
Description: This contains the officially supported and free software provided by Canonical, the company behind Ubuntu. All the packages here are open-source and come with full support.
Typical Use: This is enabled by default, and most essential packages are found here.
2. Universe Repository
Description: The Universe repository contains open-source software maintained by the community, not directly by Canonical. These packages are free to use but are not officially supported.
Typical Use: For additional software packages that aren’t in the Main repository, like development tools or niche applications.
Command to enable:
```bash
sudo add-apt-repository universe
sudo apt update
```
3. Multiverse Repository
Description: This repository contains software that is not completely free or may have legal restrictions in some countries (e.g., certain codecs or drivers).
Typical Use: For non-free software like proprietary drivers, restricted codecs, etc.
Command to enable:
```bash
sudo add-apt-repository multiverse
sudo apt update
```
4. Restricted Repository
Description: Contains proprietary drivers and firmware that are required to make certain hardware work on your system, like graphics card drivers (e.g., NVIDIA or AMD drivers).
Typical Use: For hardware support that requires proprietary drivers or firmware.
Command to enable:
```bash
sudo add-apt-repository restricted
sudo apt update
```
5. Backports Repository
Description: This repository contains newer versions of certain software that have been backported to the current stable version of Ubuntu. These packages are usually not as thoroughly tested as those in the Main repository.
Typical Use: When you need a newer version of a software package than what is available in the Main or Universe repositories.
Command to enable:
```bash
sudo add-apt-repository backports
sudo apt update
```
6. PPA (Personal Package Archives)
Description: PPAs are third-party repositories hosted on Launchpad (Ubuntu's hosting service). Developers can create PPAs to provide users with more up-to-date or specialized versions of software.
Typical Use: For software that isn’t in the official repositories or when you want newer versions than those in the official repositories.
Command to add a PPA:
```bash
sudo add-apt-repository ppa:<ppa_name>
sudo apt update
```
How to Check Your Enabled Repositories
You can check the list of enabled repositories by viewing the /etc/apt/sources.list file:

```bash
cat /etc/apt/sources.list
```
Or you can use a graphical tool like Software & Updates to enable/disable repositories:

Open the "Software & Updates" tool.
Navigate to the "Ubuntu Software" tab.
Enable/disable repositories by checking or unchecking the boxes for Main, Universe, Multiverse, and Restricted.

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