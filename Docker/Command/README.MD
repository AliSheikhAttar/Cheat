# Docker Commands

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

- start container
- -i for interactively
```bash
docker start -i <container id>
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

- Push an image to the docker registey (docker hub)
```bash
docker push <username/image name>
```

- Free unused spaces
```bash
docker container prune -f
docker image prune -f
docker volume prune -f
```

- Delete docker image
```bash
docker rmi  <image id>
```

- Delete docker dangling image Layers with no relation to labeled images are called dangling images. They’re outdated and take up unnecessary disk space. 
```bash
#list
docker images -f dangling=true
#Remove
docker image prune
```

- terminate container
```bash
docker container stop <ID_or_Name>
```

- remove container
```bash
docker container rm <ID_or_Name>
```

- Delete dangling volumes;
```bash
docker volume prune
```

- This command is used to execute a command in a running container
- otherwise pull it then run it
```bash
docker exec <container> <command>
```

- Port to container and open bash
```bash
docker exec -it <imageid> bash
```