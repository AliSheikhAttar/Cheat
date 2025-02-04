# General

- all environment variables
```bash
printenv
```
- specific environment variables
```bash
printenv <specific ev>
# or
echo $ev
```

- store environment variable in the current session/terminal session
```bash
export <ev>=<ev value>
```

- set environment variable
```bash
export <ENV_VAR>=<Value>
```

- user pesonal startup file
- linux loads the command every time a user loggs in
```bash
~/.bashrc
```

- set environmet variable permanently
```bash
echo <ev>=<ev value> >> ~/.bashrc
```

- reload the bashrc file
```bash
source ~/.bashrc
```