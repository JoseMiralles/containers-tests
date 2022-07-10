# 1. Add Env Variables

Create the [.env file](React_Flask_PSQL_Example/.env) in the root directory of the project.

Env variables can be used from TSX and TS files using `process.env`. Define `FRONTEND_PORT=3000` in there.

Example:
```
const usersURL = `${process.env.REACT_APP_API_BASE_URL}/users`
```

# 2. Create docker-compose.yml

Add the `frontend` service to docker-compose.yml. It is important to add the volumes to be able to see changes in real time.

[View docker-compose.yml file](React_Flask_PSQL_Example/docker-compose.yml)

```
version: "3"

services:

  frontend:
    build:
      context: ./frontend
      target: dev
    volumes:
      - ./frontend:/app:delegated
      - /app/node_modules
    ports:
      - ${FRONTEND_PORT}:3000
    environment:
      - REACT_APP_API_BASE_URL=http://localhost:${API_PORT}   # Example API variable
    stdin_open: true
    # depends_on:
      # - main-api    # Add dependency for a container running the main-api image which should be defined in this file as well.
```

# 3. Create react app

- In the root dir, create app with `npx create-react-app <app-name> --template typescript`
- Create a [`Dockerfile`](React_Flask_PSQL_Example/frontend/Dockerfile) in the new folder.
- Create [`.dockerignore`](React_Flask_PSQL_Example/frontend/.dockerignore) in the new folder.

# 4. Run the app

Use `docker-compose up` to run the app. The should be accessible from http://localhost:3000/ (if 3000 was set as FRONTEND_PORT).
