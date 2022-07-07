# Images

A collection of app binaries and dependencies.

## Image Commands

- `sudo docker image ls` Lists all images
- `sudo docker image tag <image> <user>/<image>` Tags an image
- `sudo docker inspect <image>` Shows metadata for image
- `sudo docker image history <image>` Shows a list of changes
- `sudo docker image rm <image>` Remove image

<br>

- `sudo docker image push <account>/<image>` Pushed image to docker hub
- `sudo docker build . -t <account>/<image>` Creates an image using the current directory's Dockerfile. It also assigns it a name.

# Example Dockerfile using two images:

```
# Use node:alpine as a base image, and give it a reference name..
FROM node:8.15-alpine as build-stage

# Create /app, and copy local contents to it.
WORKDIR /app
COPY . /app
# This runs in the '/app' directory since that is the active dir.
RUN npm install

# Use the second base image
FROM nginx:1.15
EXPOSE 80
# Copy files from previous container.
COPY --from=build-stage /app /user/share/nginx/html
COPY --from=build-stage /app/nginx.conf /etc/nginx/conf.d/default.conf

```
