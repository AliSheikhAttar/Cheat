# Permissions

## User & Group

- Group : group of users with same permissions
- User : account contains followings:
    - Username
    - User ID (UID)
    - Password
    - Primary Group (GID)
    - Location of the Home Directory
    - Default Shell
    
- with each user created a new line appended to /etc/passwd containing followings:
- > username:password:UID:GID:Extra Info:home directory:shell

- user encoded password exists in etc/shadow/

- users can have multiple secondary groups in addition to their primary (0) group


- your user
```bash
 whoami 
```
- hostname (name of the machine)
```bash
hostname
```
- more details the about user : UID , GID & all of the group IDs the user belongs to
```bash 
id 
```
- user last logged ins
```bash
last
```

- all users last logged ins
```bash
lastlog
```
- add user <user> to system with its home and bash
  - -m: Create home directory for user
  - -c: Add a comment for user
  - -s: Set default shell for user
```bash
sudo useradd -m -c "<user> Temporary User" -s /bin/bash <user>
```

- create <user> and append <group> to its groups
```bash useradd -G <group> <user> `
- set no password for <user>
```bash passwd -d <user> `
- set password for user
```bash
sudo passwd <user>
```
- list of encrypted passwords
```bash
sudo cat /etc/shadow
```
- another way to create user
```bash 
sudo adduser <user> 
```

- Create group
```bash 
sudo groupadd <group> `
```
```bash
sudo addgroup shared 
```
- Append <group> to <user> groups
```bash
sudo usermod -a -G <group> <user> 
```

- delete <user>
```bash
sudo deluser --remove-home <user> 
```

- delete <user> and its home directory
```bash
 userdel -r <user> 
```

- delete <group>
```bash
sudo delgroup <group> 
```

## root
### su
- login as user
```bash
su -
```
- login and redirect password
```bash
su - <user> << <password>
```
 
- login as user & password
```bash
sudo su -
```

- exit to owned user
```bash
exit
```

- login as other users
```bash
su - <user>
```
-c, --command=command
لاگین شدن به عنوان کاربر داده شده	-, -l, --login
استفاده از شل دلخواه به جای شل پیشفرض	-s, --shell=shell
- options
- -, -l, --login : login as inputed user
- -c, -command=command : run command without logging in as user
- -s , --shell=shell, use arbitrary shell instead of default shell

### Sudo
run commands as root
- login as root
```bash
sudo -i
```
## Files & Directories

- the first char:
  - - -> file
  - d -> directory
  
- order:
  - user owner, group owner, others
  
- r : read
- w : write
- x : execute, going to directory (cd)

rwx (111) => all permission
r-x (101) => not writable
-wx (11)  => not readable

```bash
ls -l
```
- First column : 
  - first char : 
    - - => file 
    - d => directory
  - rest :
    permissions of three:
      - owner user, owner group, others
- third :
  owner user
- fourth :
  owner group

![Permission image](permissions.png)

### Set/Change ownership

- chown: change the ownership of files/directories to <user> and <Group>
```bash
  sudo chown -c -R $USER:$USER <directory>/<file>
```
```bash
  sudo chown -c -R $USER:$USER <directory>
```
Explanation:
>-c: report all changes
>-R: do this recursively (for all files/directories beneath the given one)
>$USER:$USER: change the owner and the group that owns the the entry to the user that issues the command (sudo preserves the > > values)
> $HOME: do this with your home directory
> You can test those environment variables with the following commands
` echo $USER `
` sudo echo $USER `
` echo $HOME `
` sudo echo $HOME `

### Change permissions

- chmod : root or owner of files/directory
```bash
chmod [OPTION] [ugoa][-+=][rwx] FILE/DIR...
```
- u = user
- g = group
- o = others
- a = all (default)

- - = revoke the permissions
- + = grant new permissions
- = = revoke all previous permissions and grant new permissions

- append write permissions for file for other users
```bash
chmod o+w <file>
```

- combinig
- grand x and w permissions and revoking read permission for others and owner group
```bash
chmod og+x+w-r <file1> <file2> ... <pattern>
```

- set read and write permissions (110 = 6) for user, group and others for file (666)
```bash
chmod 666 transferred-file
```
- Remove permission
- the umask acts as a filter to remove certain permissions from the default permission set. It helps enforce security policies by restricting the default access granted to newly created files and directories.
```bash
umask <value ex. 777>
```
