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
` whoami `
- more details the about user : UID , GID & all of the group IDs the user belongs to
` id `


- add user <user> to system with its home and bash
  - -m: Create home directory for user
  - -c: Add a comment for user
  - -s: Set default shell for user
```bash
sudo useradd -m -c "<user> Temporary User" -s /bin/bash <user>
```

- create <user> and append <group> to its groups
` useradd -G <group> <user> `
- set no password for <user>
` passwd -d <user> `
- set password for user
```bash
sudo passwd <user>
```
- login as user
` su - <user> `
- another way to create user
` sudo adduser <user> `

- Create group
` sudo groupadd <group> `
` sudo addgroup shared `

- Append <group> to <user> groups
` sudo usermod -a -G <group> <user> `

- delete <user>
` sudo deluser --remove-home <user> `

- delete <user> and its home directory
` userdel -r <user> `
- delete <group>
` sudo delgroup <group> `



## Change ownership

- change ownership of directories
```bash
  sudo chown -c -R $USER:$USER <directory>
```
Explanation:
>chown: change the ownership of files/directories
>-c: report all changes
>-R: do this recursively (for all files/directories beneath the given one)
>$USER:$USER: change the owner and the group that owns the the entry to the user that issues the command (sudo preserves the > > values)
> $HOME: do this with your home directory
> You can test those environment variables with the following commands
` echo $USER `
` sudo echo $USER `
` echo $HOME `
` sudo echo $HOME `

## root
