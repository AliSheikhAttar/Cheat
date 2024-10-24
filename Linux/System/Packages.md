## apt

> dpkg --> apt-get, aptitude --> Synaptic, Software Center

- install .deb package
```bash
sudo dpkg -i <DEB_PACKAGE>
```

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

### dpkg

Packages are manually installed via the dpkg command (Debian Package Management System). dpkg is the backend to commands like apt-get and aptitude, which in turn are the backend for GUI install apps like the Software Center and Synaptic.

Something along the lines of:

dpkg --> apt-get, aptitude --> Synaptic, Software Center

But of course the easiest ways to install a package would be, first, the GUI apps (Synaptic, Software Center, etc..), followed by the terminal commands apt-get and aptitude that add a very nice user friendly approach to the backend dpkg, including but not limited to packaged dependencies, control over what is installed, needs update, not installed, broken packages, etc.. Lastly the dpkg command which is the base for all of them.

Since dpkg is the base, you can use it to install packaged directly from the command line.

- Install a package
```bash
sudo dpkg -i DEB_PACKAGE
```
For example if the package file is called askubuntu_2.0.deb then you should do sudo dpkg -i askubuntu_2.0.deb. If dpkg reports an error due to dependency problems, you can run sudo apt-get install -f to download the missing dependencies and configure everything. If that reports an error, you'll have to sort out the dependencies yourself by following for example How do I resolve unmet dependencies after adding a PPA?.

- Remove a package
```bash
sudo dpkg -r PACKAGE_NAME
```
For example if the package is called askubuntu then you should do sudo dpkg -r askubuntu.

- Reconfigure an existing package
```bash
sudo dpkg-reconfigure PACKAGE_NAME
```
This is useful when you need to reconfigure something related to said package. Some useful examples it the keyboard-configuration when you want to enable the Ctrl+Alt+Backspace in order to reset the X server, so you would the following:
```bash
sudo dpkg-reconfigure keyboard-configuration
```
Another great one is when you need to set the Timezone for a server or your local testing computer, so you use use the tzdata package:
```bash
sudo dpkg-reconfigure tzdata
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