# docker compose

- version of doker compose compatible with docker engine version
```yaml
version: "<version>"
```

- service and images of application
> defining various services and tell docker how to build image for each services and how to run each image

- environment variables
> for example our backend services should know about where are the databse, 
> so we specify with environment variables

- share source code with container
> install dependencies in host machine first
```yml
volumes:
  - <relative path to directory on host>:<path to directory on container>
```

- override CMD command inside the dockerfile with <command>
```yml
command: <command> && <command> ...
```

- run test inside container
> its slower than running test seperately for each 
> for example for api test

```yml
  api:
    build: <dockerfile location: ./backend>
    ports:
    - <port on host:3000>:<port on container:3000>
    environment:
    - DB_URL=mongodb://<host on docker network:db>/<database>
    # or
    - DB_URL: mongodb://db/database
    volumes:
    - <relative path to directory on host>:<path to directory on container>

    command: ./<sh file> && <command> && <command> ...

  api-tests:
    image: <app name>_<service to test>
    volumes:
      - <./backend>:</app>
    command: <command to run test>

```

```yml
version: "<version>"

services:
    web:
      build: <dockerfile location: ./frontend>
      ports:
        - <port on host:3000>:<port on container:3000>
    api:
      build: <dockerfile location: ./backend>
      ports:
        - <port on host:3000>:<port on container:3000>
      environment:
        - DB_URL=mongodb://<host on docker network:db>/<database>
        # or
        - DB_URL: mongodb://db/database
      volumes:
        - <relative path to directory on host>:<path to directory on container>
    
      command: ./<sh file> && <command> && <command> ...
    db:
      image: <image to pull from dockerhub: mongo4.0-xenial>
      ports:
        - <port on host:27017>:<port on container:27017>
      volumes:
        - <volume>:<directory on container>

volumes:
  <volume>:
```