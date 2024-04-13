# Docker File

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

- restart if stoped
```bash
restart: always
```