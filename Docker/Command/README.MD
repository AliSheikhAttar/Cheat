# Docker Commands

- info on commands
```bash
docker <command> --help
```

- package our application
> -t for tag
```bash
docker build -t <image name> <build context: .>
```

- specify the name for dockerfile
```bash
docker build -t <image name> -f <dockerfile name: Dockerfile.prod> <build context: .>
```

## List
- list all the running Docker containers
```bash
docker ps
```

- List all the containers including stopped ones
```bash
docker ps --all/-a
```

- container ids list
```bash
docker container ls -q
```

- containers list
```bash
docker container ls -a
```

- list all the Docker images 
```bash
docker images
```
```bash
docker image ls
```
- list only image ids
```bash
docker image ls -q
```

- List of images with sizes
```bash
docker compose images
```

- list of available Docker volumes
```bash
docker volume ls  
```

- List of dangling volumes; A dangling volume is a volume that exists but is no longer attached to any container.
```bash
docker volume ls -f dangling=true 
```

- Available resources
```bash
docker  container ls
docker  image ls
docker  volume ls
docker  network ls
docker  info
```

- pull image
```bash
docker pull <image>
```

## Container logs
- see logs of a container
> for example output of the websere in the terminal when we run locally
```bash
docker logs <container id>
```

- see logs in real time continuesly
```bash
docker logs -f/--follow <container id>
```

- see last <n> lines of log
```bash
docker logs -n 5 <container id>
```

- see timestamps of (lines of) logs
```bash
docker logs -t <container id>
```

## docker run
- run image as container if locally available
- start a new container
```bash
docker run <image>
```

- run image as container if locally available then run <command> in it
```bash
docker run <image> <command>
```

- run image as container if locally available in the background (detached mode)
```bash
docker run -d <image>
```

- naming containers
```bash
docker run -d --name <container name> <image> 
```

- publish a port on the host to port on container
```bash
docker run -p <machine port>:<container port>
```

- start container and interact with it (open shell)
```bash
docker run -it <image>
```

## start, exec, interact
- start stoped container
- -i for interactively
```bash
docker start -i <container id>
```

- This command is used to execute a command in a running container
otherwise pull it then run it
```bash
docker exec <container name/container id> <command>
```

- Stop container
```bash
docker stop <container>
```

- run by bash session
```bash
docker exec -it <container id> bash
```

- login as user into linux container
```bash
doker exec -it -u <user> <container id> bash
```

- Restart one or more Docker containers that are currently operating. Restarting a container entails gently pausing it and then restarting it with the same configuration and parameters.  It is recommended to use this after rebooting the system.
```bash
docker restart <container container2 ...>
```

- Copying files between the host and containers
- from container to host
```bash
docker cp <containerID>:<full path to file or dir in container ex:/app/log.txt> <destination on host ex: .>
```
- from host to container
```bash
docker cp <host path ex:secret.txt> <containerID>:<container path ex:/app>
```

- Create a mapping/binding between a dir on the host and a dir in the container
> we can also bind named volumes if we want with -v option
```bash
docker run -v <dir full path on the host ex:$(pwd)>:<dir in the container filestystem ex:/app>
```

## Volume
- create volume
- this would be dir that docker manages
```bash
docker volume create <volume name>
```

- inspect volume
```bash
docker volume inspect <volume name>
```

- map volume on local directory or cloud platform to a directory in container filesystem
> if the volume doesn't exist, docker will create a new one
> same goes for directory in container filesystem
> if let the docker create the directory, the directory will be owned by root (limited previleges for normal user)
```bash
docker run -v <volume name>:<absolute path to directory in the filesystem> <image>
```

## Stop, kill, delete
- terminate container
```bash
docker container stop <ID_or_Name>
```

- remove a stopped container
```bash
docker container rm <ID_or_Name>
# or
docker rm <ID_or_Name> <ID_or_Name> ...
```

- force remove a running container
```bash
docker rm -f <ID_or_Name>
```
- Stop the container immediately by killing its execution. While the ‘docker stop’ command helps shut down the container in its own time, the ‘docker kill’ command stops it at once.
```bash
docker kill <container>
```

- search for image
```bash
docker search <image name>
```

- Delete docker image
```bash
docker rmi  <image id>
```

- Delete docker dangling/loose image Layers with no relation to labeled images are called dangling images.No name & tag. They’re outdated and take up unnecessary disk space. 
```bash
#list
docker images -f dangling=true
#Remove
docker image prune
```

- delete containers running old/dangling images / stopped containers
```bash
docker container prune
```

- Delete dangling volumes;
```bash
docker volume prune
```

- Free unused spaces
```bash
docker container prune -f
docker image prune -f
docker volume prune -f
```

- delete an image
```bash
docker image rm <image name1/image id1> <image2> ...
```

- delete all images
```bash
docker image rm $(docker image ls -q)
```

## Tag & Push to registery

### versioning
- tagging during build
```bash
docker build -t <image name>:<tag> <dockerfile location>
```

- tagging after build
```bash
docker image tag <image name>:<default/latest tag> <image name>:<tag>
## or
docker image tag <image id> <image name>:<tag>
```
- change the image pointing to by a specific tag
```bash
docker image tag <new image id> <old image name>:<tag>
```

- delete a tagged image
```bash
docker image remove <image name>:<tag>
```

### Push/pull to/from registery
- change the repository
```bash
docker image tag <image id> <dockerhub username>/<image name on dockerhub>:<tag>
```

- login to docker
```bash
docker login
```
- Push an image to the docker registery (docker hub)
```bash
docker push <dockerhub username>/<image name on docker hub>:<tag>
```

- compress image and save to a tar archive or STDOUT
```bash
docker image save -o <file>  <image:tag>
```

- load an image from a tar archive or STDIN
> the loaded image would have the same image id as the image which was saved
> -q -> suppress the load output
```bash
docker image load -i <file>
```

## docker compose

- build images (using catch)
```bash
docker-compose build
# or
docker compose build
```
- specify docker-compose yml file
```bash
docker-compose -f docker-compose.prod.yml build
# or
docker compose build
```

- force full rebuild images (without using cache)
```bash
docker-compose build --no-cache
# or 
docker compose build --no-cache
```

- start/start app
- start container (build and start images not available) 
```bash
docker-compose up
```
- start container in the background
```bash
docker-compose up -d
```
- rebuild every time start app
```bash
docker-compose up --build
```

- all the relevant containers to the application
```bash
docker-compose ps
```

- stop and remove containers
```bash
docker-compose down
```

- view all logs across all containers of application in one place
> continuosly see new messages with -f option
```bash
docker-compose logs -f
```


## network
> when we start app using docker compose, the docker create network and add containers to the network
> docker have embedded dns server that map ips to services name
> each container contains a dns resolver which talks to dns server to resolve host names

## docker-machine / Deploy
> in production environment:
> we won't need volumes for sharing source code
> we won't need test containers to continuosly run -> slows down server

- vps
- create vps using docker-machine
> create virtual machine and install docker on it
> we will be able to talk to that docker engine remotely on our machine
```bash
docker-machine create \
--driver digitalocean (none for personal server) \
--digitalocean-access-token <token> \
<server name>
```

- connect to server via ssh
> from here every command we execute will be sent to docker engine on the vps
```bash
docker-machine ssh <server name>
```

- list of docker machines and ip of our server: webserver
```bash
docker-machine ls
```

- list of environment variables we need to set to talk to the production machine
```bash
docker-machine env <server name / production machine>
```

- set environment variables
> the docker machine will be active
```bash
eval $(docker-machine env <production machine>)
```

- deploy
> docker-compose.prod.yml on our local machine
```bash
docker-compose -f <docker-compose.prod.yml> up -d
```

