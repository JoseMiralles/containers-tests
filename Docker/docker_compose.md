# Docker Compose

Most important features:

- Allows to deploy multiple containers.
- Automatic network config.
- Preserves volume data automatically.
- Only recreates containers that have changed.
- Varibales can be used.

Structure of `docker-compose.yml` files:
```
# If no version is specified, then version 1.0 is assumed. 
# Recommend version 2 at the minimum
version: '3.1'  

services:  # Will start up containers (is the same as using docker container run).
servicename: # Friendly name (postgres, node, etc.), also the DNS name inside your network.
  image: # Image this service will use
  command: # Optional, will replace the default CMD specified by the image
  environment: # Optional, same as -e in docker container run
  volumes: # Optional, same as -v in docker container run
psql: # servicename2

volumes: # Optional, same as docker volume create

networks: # Optional, same as docker network create
```

## Bash Completition

https://docs.docker.com/compose/completion/

# Commands

- `docker-compose --help`
- `docker-compose up` Setup volumes, networks, and start specified containers.
- `docker-compose up --build` Rebuild images before up.
- `docker-compose down` Stop and remove all containers.
- `docker-compose down -v` Same, but also removes volumes.

# Example docker-file.yaml
```
version: '3'
services:
  webapp:
    #  the build command tells compose it's building this image
    build: 
        # Will build in the current directory   
        context: .
        dockerfile: whateverthenameis.Dockerfile
        #  by passing a name here you are telling compose to name and tag the built image by this name
    image: whateverImage:whatevertag
    ports: 
        - '80:80'
```