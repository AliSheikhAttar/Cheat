

## apt
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
 