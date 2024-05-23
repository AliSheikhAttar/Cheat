# Permissions

## Basics
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

- change ownership of directories
```bash
  sudo chown -c -R $USER:$USER <directory>
```
- add user to app group
```bash
  sudo usermod -a -G <app> <user>
```
Explanation:
chown: change the ownership of files/directories
-c: report all changes
-R: do this recursively (for all files/directories beneath the given one)
$USER:$USER: change the owner and the group that owns the the entry to the user that issues the command (sudo preserves the values)
$HOME: do this with your home directory
You can test those environment variables with the following commands

echo $USER
sudo echo $USER
echo $HOME
sudo echo $HOME
