# Users n Groups
## Users

- user accounts
```bash
/etc/passwd
```

- user passwords
```bash
/etc/shadow
```

- Add/modify/delete user
```bash
user<add/mod/del> <username>
```

- perl script which is more interactively than useradd (use useradd under the hood)
```bash
adduser 
```

### options for useradd
- -m -> create home directory

### options for usermod
- -s -> set shell
- -g <group> <user>-> set primary group
- -G -> set supplemental group

## Groups
- all users in the same group have a same permissions
- primary group owns the user files
- all the groups
```bash
cat /etc/group
```

- groups of a user
```bash
groups <user>
```

- Add/modify/delete group
```bash
group<add/mod/del> <groupname>
```
 