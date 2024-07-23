# SSH
## How it works
An SSH connection between the client and server occurs in three main stages:

- 1. Server Authentication by Client

The client initiates an SSH connection request to the server, which listens on the default port 22 (this port is configurable). At this stage, the server's identity is verified:
If the client is accessing the server for the first time, it is prompted to manually authenticate the server's public key, which can be found using ssh-keyscan or online resources like Google. After confirmation, the server's key is added to the known_hosts file in the ~/.ssh directory on the client machine. This file contains information about all servers authenticated by the client.
If the client has previously connected to the server, the server's identity is verified against the previously recorded information in the known_hosts file.

- 2. Session Key Generation

After server authentication, both parties negotiate to generate a session key using a key exchange algorithm like Diffie-Hellman. The session key is a shared symmetric key used for both encryption and decryption.

- 3. Client Authentication

After generating the session key, client authentication is performed using SSH key pairs:
The process begins with the client sending the ID of the key pair it wants to use for authentication to the server.
The server checks the authorized_keys file and the corresponding account for that ID.
If a public key with that ID is found, the server generates a random number (preferably a large prime for security), encrypts it with the corresponding public key, and sends the encrypted message to the client.
If the client has the correct private key, it decrypts the message to obtain the random number.
The client combines the obtained number with the session key, hashes it (using modern algorithms like SHA256), and sends the hashed response to the server.
Finally, the server hashes the initial random number with the session key using the same algorithm and compares it with the client's response. If they match, it proves the client has the correct private key, and the client is authenticated.

## Setup
### install client
```bash
sudo apt update && sudo apt install openssh-client
```

### install server
```bash
sudo apt install openssh-server
```
### connect to linux server
```bash
ssh [username]@[host_ip_address]
```
-p : server SSH port (default = 22)

### create public & private keys
this will create the pair of keys in ~/.ssh/ directory
```bash
ssh-keygen -t <type of key to encrypt> -C <comment>
```
type of key to encrypt: RSA ECDSA Ed25519

### use ssh keys without passphrase

- output of ssh-agent(tool to handle private keys)
```bash
SSH_AUTH_SOCK=/tmp/ssh-XXXXXXXXX/agent.<pid>; export SSH_AUTH_SOCK;
SSH_AGENT_PID=<pid>; export SSH_AGENT_PID;
echo Agent pid <pid>;
```

##### create private key
```bash
eval "$(ssh-agent -s)"
```
- -s => format the output adhere to bash shell syntax

##### add private key to ssh-agent
```bash
ssh-add ~/.ssh/id_<type of key used = ed25519>
```

##### add public key to server authorized keys

```bash
ssh-copy-id -i ~/.ssh/id_<ed25519>.pub your_username@ip_address_of_server
```

##### login without password to server
```bash
ssh <your_username>@<ip_address_of_server>
```

##### disable password in server ssh config
```bash
/etc/ssh/sshd_config => PasswordAuthentication no
```

## Access & Transfer & Managing of files
### **Protocols : RCP(dont encrypt => use telnet) & SCP(encrypt => use  SSH)**
```bash
scp [options] <source_file_or_directory> <destination_file_or_directory>
```

#### copy local dir to server
```bash
scp -r <directory> <remote_user@remote_host:/path/to/directory>
```
- accesses : 4 =< in local & 2 <= in remote

### **Protocols :  SFTP (Secure File Transfer Protocol) newer & safer than  FTP (File Transfer Protocol)**
#### loging to server
```bash
sftp username@remote-server
```

* use l in the beginning of commands to command in local else in server
#### cd in local
```bash
sftp> lcd /path/to/local/directory
```

#### cd in server
```bash
sftp> cd /path/to/remote/directory
```

#### upload file on server
```bash
sftp> put example.txt
```

#### download from server
```bash
sftp> get example.txt
```

#### exit
```bash
exit
```

