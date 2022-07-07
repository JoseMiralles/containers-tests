# Commands

- View running containers: `sudo docker container ls`
- View all containers: `sudo docker container ls -a`
- Inspect container: `sudo docker container inspect <container-name>`
- Start container: `sudo docker container start <container-name> <container-name> ...`
- Stop container: `sudo docker container stop <container-name> <container-name> ...`
- Delete container: `sudo docker container rm <container-name> <container-name> ...`
- View logs: `sudo docker container logs <name>`
- View Networks: `sudo docker network ls`

### Example, opening psql on running postgres container:
`docker exec -it <container> psql -U postgres`

# Create Containers, examples:

## Nginx container
Create a container with the nginx image. It should be detached, and with the name `nginx`. The internal host IP should be 80 and the container ip should be 80.

`sudo docker container run -d -p 80:80 --name nginx nginx`

Open: http://localhost:80

Breakdown:
- `-d`: Detached.
- `-p`: Port and local ip.
- `--name nginx`: The unique name to give this container.
- `nginx`: The image to use for this container.

## (Apache) httpd container

Container needs to be detached. Find the intended port by going here, and opening the link to the docker file. The intended port would be assigned to `EXPOSE`.

`sudo docker container run -d -p 8080:80 --name apache httpd`

Open: http://localhost:8080

## MySQL container

Create a detached container with the `mysql` image. Use these ports: `3306:3306`. Pass in the following enviroment variable: `MYSQL_ROOT_PASSWORD=admin1234`

`sudo docker container run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=admin1234 --name mysql mysql`

- Check the env variable: `sudo docker container inspect mysql`


# Create container with CLI access

Use the `i` and `t` flags.

`sudo docker container run -it nginx`

- `-t` Simulates a terminal.
- `-i` Keeps a session open to receive terminal input.

The container stops once the CLI is closed.

## Start existing container with CLI access

1. Start container: `sudo docker container start <name>`
2. Then run: `sudo docker exec -it <name> bash`

The container will still remain running even after exiting from its CLI.

It is possible to use `-d` and `-t` flags to keep the container running:

`sudo docker container run -d -t <image>`

# Containers and networking

## --net-alias <alias>

This allows multiple containers to act as if they are on the same network.

Example, create two elastisearch containers with the --net-alias `dns`:

`sudo docker container run -d --net-alias dns --name dns elastisearch:2`
`sudo docker container run -d --net-alias dns2 --name dns elastisearch:2`

# Binding container to directory

This allows for a directory and its contents to be edited by the host machine, and the bound container.

https://docs.docker.com/storage/bind-mounts/

# Creating a Volume

These are better since they are easier to package.

https://docs.docker.com/storage/volumes/