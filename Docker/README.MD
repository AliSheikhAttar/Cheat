# Docker

- Building

```bash
docker-compose build
```
- Run All Containers

```bash
docker-compose up
```

- Delete All Containers
```bash
docker-compose down
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

- package 
```bash
FROM python:3
```

```bash
ENV PYTHONUNBUFFERED=1
```

```bash
WORKDIR /app
```

```bash
COPY requirements.txt ./
```

```bash
COPY . .
```

- make a specific port accessible to other services within the same network.
```bash
EXPOSE 8080
```

- Port Forwarding:map port from docker container to local machine
```bash
docker run -p <local port>:<container port> <image id>
```
- make port accessible for all services connected to host machine
```bash
ports:
      - "<local port>:<container port>"
```

- run command in terminal
```bash
RUN pip install -r requirements.txt
```

- command
```bash
CMD ["python", "manage.py", "runserver"]
```

- Share Database data across multiple containers
```bash
    volumes:
    - db-data:
```

- mount volume in container 
```bash
    volumes:
    - db-data:/<dir name>
```
