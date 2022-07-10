# 1. Add Env Variables

Create the [.env file](React_Typescript_Docker/.env) in the root directory of the project.

Env variables can be used from TSX and TS files using `process.env`.

Example:
```
const usersURL = `${process.env.REACT_APP_API_BASE_URL}/users`
```

# 2. Create docker-compose.yml

It is important to add the volumes to be able to make changes real time.

[View docker-compose.yml file](React_Typescript_Docker/docker-compose.yml)

# 3. Create react app

- In the root dir, create app with `npx create-react-app <app-name> --template typescript`
- Create a `Dockerfile` in the new folder.
- Create `.dockerignore` in the new folder.

# 4. Run the app

Use `docker-compose up` to run the app.
