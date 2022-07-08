# .env variables in docker-compose.yml

1. Create `.env` in root folder alongside `docker-compose.yml`
2. Add a var to it: `BACKEND_CATALOG_MANAGEMENT_PORT=8081`
3. Include the new variable in `docker-compose.yml`

```
version: '3.8'
services:
  catalog-management:
    ...
    ports:
      - ${BACKEND_CATALOG_MANAGEMENT_PORT}:${BACKEND_CATALOG_MANAGEMENT_PORT}
    volumes:
        ...
```

## Use .env to define project name for images

Add the following var to the root `.env` file: `COMPOSE_PROJECT_NAME=<project_name>`