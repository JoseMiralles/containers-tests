# 1. Create .env file

Add the api port, database name, as well as the database password and username to the [.env file](React_Flask_PSQL_Example/.env).

# 2. Create docker-compose.yml

Add the service for the api to the [docker-compose.yml](React_Flask_PSQL_Example/docker-compose.yml) file.

Include the database and the network to limit access to the database.

# 3. Add other docker files and .gitignore files.

- Create [Dockerfile](React_Flask_PSQL_Example/backend/Dockerfile)
- Create [.dockerignore](React_Flask_PSQL_Example/backend/.dockerignore)
- Create [.gitignore](React_Flask_PSQL_Example/backend/.gitignore)
- Add [wait-for file](React_Flask_PSQL_Example/backend/wait-for). This is great for when it is necessary to wait for another container to be created before running a command.
- Create [requirements.txt](React_Flask_PSQL_Example/backend/requirements.txt) with all of the pip packages necessary.

# 4. Add app.py