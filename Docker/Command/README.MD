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

The command run overrides the command defined in the service configuration.
For example, if the web service configuration is started with bash, then docker-compose run web python app.py overrides it with python app.py.
```bash
docker compose run <image> [command]
```
The second difference is the docker-compose run command does not create any of the ports specified in the service configuration.
This prevents the port collisions with already open ports. If you do want the service's ports created and mapped to the host, specify the --service-ports flag:
```bash
$ docker-compose run --service-ports web python manage.py <command Ex:shell>
```

- login
```bash
docker login -u <username> -p <password>
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

- Free unused spaces
```bash
docker container prune -f
docker image prune -f
docker volume prune -f
```

- Delete all Containers
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
- List of containers
```bash
docker ps
```

- List of containers with sizes
```bash
docker images
```

- Available resources
```bash
docker  container ls
docker  image ls
docker  volume ls
docker  network ls
docker  info
```
- Available volumes
```bash
docker volume ls
```
- Create volume
```bash
docker create volume <volume name>
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

- containers list
```bash
docker container ls -a
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

- list of available Docker volumes
```bash
docker volume ls  
```

- Delete 1/more volumes
```bash
docker volume <rm vol_name vol_name2>  
```

- List of dangling volumes; A dangling volume is a volume that exists but is no longer attached to any container.
```bash
docker volume ls -f dangling=true 
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

- Delete docker network;If you get errors, remove the containers using the network.
```bash
docker network rm <networkID>
```

- Inspection
```bash
docker inspect 
```
