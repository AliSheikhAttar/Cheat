# Docker Commands

- info on commands
```bash
docker <command> --help
```

- package our application
> -t for tag
```bash
docker build -t <image name> <dockerfile location>
```

- list all the running Docker containers
```bash
docker ps
```

- List all the containers including stopped ones
```bash
docker ps --all/-a
```

- list all the Docker images 
```bash
docker images
```
```bash
docker image ls
```

- containers list
```bash
docker container ls -a
```

- list of available Docker volumes
```bash
docker volume ls  
```

- List of dangling volumes; A dangling volume is a volume that exists but is no longer attached to any container.
```bash
docker volume ls -f dangling=true 
```

- List of images with sizes
```bash
docker compose images
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

- run image as container if locally available
```bash
docker run <image>
```

- start container and interact with it (open shell)
```bash
docker run -it <image>
```

- run image as container if locally available then run <command> in it
```bash
docker run <image> <command>
```

- start container
- -i for interactively
```bash
docker start -i <container id>
```

- This command is used to execute a command in a running container
otherwise pull it then run it
```bash
docker exec <container> <command>
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

- delete containers running old/dangling images
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

- terminate container
```bash
docker container stop <ID_or_Name>
```

- remove container
```bash
docker container rm <ID_or_Name>
```

## Tag & Push to registery
> versioning
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

### Push to registery
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


- Copying files between the host and containers
```bash
docker cp <containerID>:/app/log.txt .
```
```bash
docker cp secret.txt <containerID>:/app
```