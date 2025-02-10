# Docker File

## FROM
- base image
```dockerfile
FROM <base image>:<linux distro>
```
```dockerfile
FROM <node>:<alpine>
```

- label
> seperate the stages of operation
> reference to the stages
```dockerfile
FROM <base image>:<linux distro> AS build-stage
```

## COPY ADD

- change the working directory (cd in linux)
```dockerfile
WORKDIR /app
```

- copy all files from current dir to app dir in node image filesystem
```dockerfile
COPY . /app
```

- copy all files from current dir to current working dir in image filesystem
```dockerfile
COPY . .
```

- copy from specific stage from the dockerfile
```dockerfile
COPY --from=<label: build-stage> <directory in the stage: /app/build> <dest dir in this stage>
```

- ADD is COPY with two more features
- Copy Files from url
```dockerfile
ADD https://.../file .
```
- uncompress a file to working dir in image
```dockerfile
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
* we can have single CMD but multiple RUN
- execute commands like ones executed in terminal session
```dockerfile
RUN <CMD>
```

- default command to be executed after build
```dockerfile
CMD <command>
```
```dockerfile
CMD node app.js
```

- shell form
> docker will execute inside a seperate shell
```dockerfile
CMD <npm> <start>
```
- exec form
> execute directly, easier and faster to clean up resources when containers stop
```dockerfile
CMD ["npm", "start"]
```
- to overwrite CMD
```bash
docker run <image> <command>
```

- ENTRYPOINT similar to CMD harder to get overwriten when running container
- execute everytime we start the image, no exception
```dockerfile
ENTRYPOINT ["npm", "start"]
```
- to overwrite ENTRYPOINT
```bash
docker run --entrypoint <cmd>
```

## Env variables
```dockerfile
ENV <EV>=<Value>
# or 
ENV <EV> <Value>
```

## Port 
container will lesson on <port> (on container)
```dockerfile
EXPOSE <Port>
```

## User
- all of the following commands after this will be executed as <user>
```dockerfile
# RUN addgroup <user> && adduser -S -G <user> <user>
USER <user>
```

## Build light-weight image for production
every framework have this feature that allows us to build our project files into smaller size for production

- webserver for deployment
```dockerfile
FROM nginx:1.12-alpine 
```

## Example dockerfile for lightweight image ready for production
```dockerfile
FROM node:<version>-alpine<version> AS build-stage
WORKDIR /app
COPY package*.json
RUN npm install
COPY . .
RUN npm run build

# step 2 : Production
FROM nginx:1.12-alpine
RUN addgroup app && adduser -S -G app app
USER app
COPY --from=build-stage /app/build </usr/share/nginx/html>
EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]
```
> standard path for serving files using nginx : `/usr/share/nginx/html`
> 