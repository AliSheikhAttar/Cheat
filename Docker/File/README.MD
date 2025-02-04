# Docker File

```bash
FROM <base image>:<linux distro>
```
```bash
FROM <node>:<alpine>
```

- copy all files from current dir to app dir in node image filesystem
```bash
COPY . /app
```

- change the working directory (cd in linux)
```
WORKDIR /app
```

- executing command
```bash
CMD <command>
```
```bash
CMD node app.js
```

- package our application
```bash
docker build -t <image name> <dockerfile location>
```
> -t for tag

