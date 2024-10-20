# Docker Commands

- Building & running
    - The following only builds the images, does not start the containers:
    ```bash
    docker-compose build
    ```
    - The following builds the images if the images do not exist and starts the containers:
    ```bash
    docker-compose up
    ```

    - If you add the --build option, it is forced to build the images even when not needed:
    ```bash
    docker-compose up --build
    ```

    - The following skips the image build process;If the images aren't built beforehand, it fails:
    ```bash
    docker-compose up --no-build
    ```

    - The --no-cache option disables the Docker build cache in the image creation process. This is used to cache each layer in the Dockerfile and to speed up the image creation reusing layers (~ Dockerfile lines) previously built for other images that are identical.
    ```bash
    docker-compose up --no-cache
    ```

    - Build an image from a specified docker file
    ```bash
    docker build <path to docker file>
    ```

The command run overrides the command defined in the service configuration.
For example, if the web service configuration is started with bash, then docker-compose run web python app.py overrides it with python app.py.
```bash
docker compose run <image> [command]
```
The second difference is the docker-compose run command does not create any of the ports specified in the service configuration.
This prevents the port collisions with already open ports. If you do want the service's ports created and mapped to the host, specify the --service-ports flag:
```bash
docker-compose run --service-ports web python manage.py <command Ex:shell>
```

- login
```bash
docker login -u <username> -p <password>
```

- Log out or remove the credentials used to authenticate with a Docker registry. 
```bash
Docker Logout  [REGISTRY_URL]
```


- Restart docker-machine
```bash
docker-machine restart default
```

- Reset to default env
```bash
eval $(docker-machine env default)
```

- Config
```bash
docker-compose config
```

- Run All Containers

```bash
docker-compose up
```

- Stop and remove containers, networks
```bash
docker-compose down
```

- Delete all containers and volumes
```bash
docker-compose down -v
```
- List of containers
```bash
docker-compose ps
```
- list all the running Docker containers
```bash
docker ps
```

- List all the running containers in the background
```bash
docker ps --all/-a
```

- list all the Docker images that are currently available on your system
```bash
docker images
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

- Examine the evolution of a Docker image or its constituent parts.

```bash
docker history <image_name>
```

- This command is used to execute a command in a running container
```bash
docker exec <container> <command>
```



- stop a running container.
```bash
docker stop
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
- pull image
```bash
docker pull <image>
```
- Creates a new image of an edited container on the local system
```bash
docker commit <conatainer id> <username/imagename>
```

- Push an image to the docker hub repository
```bash
docker push <username/image name>
```
- Create volume
```bash
docker create volume <volume name>
```

- Copies files or directories from the host machine’s file system to the container’s file system during Docker image construction.

```bash
COPY <source_file> <destination_directory>
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

- Delete all docker image
```bash
docker rmi $(docker images -q) 
```

- Delete docker image
```bash
docker rmi $(docker images -q) 
```


- Delete docker dangling image Layers with no relation to labeled images are called dangling images. They’re outdated and take up unnecessary disk space. 
```bash
docker images -f dangling=true
#Remove
docker image prune
```

- terminate container
```bash
docker container stop <D_or_Name ID_or_Name>
```

- terminate all containers
```bash
docker container stop $(docker container ls -aq)
```

- remove container
```bash
docker container rm <D_or_Name ID_or_Name>
```

- remove all containers
```bash
docker container rm $(docker container ls -aq)
```

- Delete 1/more volumes
```bash
docker volume <rm vol_name vol_name2>  
```


- Delete dangling volumes;
```bash
docker volume prune
```

- Port to container
```bash
docker exec -it <image> bash
```

- List of existing docker networks; Docker networks allow containers to freely connect while preventing traffic from leaving the network. 
```bash
docker network ls
```
- Create network
```bash
docker network create <network_name>
```

- Delete docker network;If you get errors, remove the containers using the network.
```bash
docker network rm <networkID>
```

- Inspection
```bash
docker inspect 
```

- docker compose alpha    -> 	Experimental commands
- docker compose create	<service>  ->  Creates containers for a service
- docker compose events	  ->  Receive real time events from containers
- docker compose logs	  ->      View output from containers
- docker compose ls	      ->  List running compose projects
- docker compose pause	  ->  Pause services
- docker compose top	  ->      Display the running processes
- docker compose version  ->    Show the Docker Compose version information
- docker compose wait	  ->    Block until the first service container stops
- docker compose watch	  ->  Watch build context for service and rebuild/refresh containers when files are updated