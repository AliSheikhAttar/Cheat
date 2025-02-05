# Docker File

## FROM
- base image
```bash
FROM <base image>:<linux distro>
```
```bash
FROM <node>:<alpine>
```
## COPY ADD

- change the working directory (cd in linux)
```bash
WORKDIR /app
```

- copy all files from current dir to app dir in node image filesystem
```bash
COPY . /app
```

- copy all files from current dir to current working dir in image filesystem
```bash
COPY . .
```

- ADD is COPY with two more features
- Copy Files from url
```bash
ADD https://.../file .
```
- uncompress a file to working dir in image
```bash
ADD file.zip .
```

- Exclude files and directories
- write directories in .dockerignore file
```bash
.dockerignore
```

## RUN CMD

* RUN is build-time instruction (during build)
* CMD is runtime instruction (executed when starting container)
- execute commands like ones executed in terminal session
```bash
RUN <CMD>
```

- default command to be executed after build
```bash
CMD <command>
```
```bash
CMD node app.js
```

- shell form
> docker will execute inside a seperate shell
```bash
CMD <npm> <start>
```
- exec form
> execute directly, easier and faster to clean up resources when containers stop
```bash
CMD ["npm", "start"]
```
- to overwrite CMD
```bash
docker run <image> <command>
```

- ENTRYPOINT similar to CMD harder to get overwriten when running container
```bash
ENTRYPOINT ["npm", "start"]
```
- to overwrite ENTRYPOINT
```bash
docker run --entrypoint <cmd>
```

## Env variables
```bash
ENV <EV>=<Value>
# or 
ENV <EV> <Value>
```

## Port 
container will lesson on <port> (on container)
```bash
EXPOSE <Port>
```

## User
- all of the following commands after this will be executed as <user>
```bash
# RUN addgroup <user> && adduser -S -G <user> <user>
USER <user>
```