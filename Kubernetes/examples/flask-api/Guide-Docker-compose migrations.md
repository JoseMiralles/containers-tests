
# 1. Use docker-compose to run migrations.

This is going to make it possible to run commands like `alembic init` from the container, and have the changes reflected in the local host file system.

1. In `/flask-api` create:
    - `app.py`  Just add some basic logic for now, like a single route to test.
    - `requirements.txt`
    - `Dockerfile`
    - `.dockerignore`
2. Create `docker-compose` and run it.
    - Notice `- ./flask-api:/usr/src/app:rw` under volumes.
    - Run with `docker-compose up --build`
3. On a new terminal, run: `docker exec -it <container-name> /bin/sh` To upen the cli on that container.
    - Use `docker container ls` to view the name of all running containers.
4. On the container cli, run `flask db init` to initialize alembic, these changes should be reflected on the local project directory.