# ApiLogicProject using Docker and docker-compose

## Installation

```
# git clone https://github.com/thomaxxl/als-docker
# cd als-docker
```

## Configure

To configure the ApiLogicProject, change the environement variables in [docker-compose.yml](docker-compose.yml):
```
    api-logic-server:
        environment:
            - APILOGICPROJECT_CLIENT_URI=//192.168.109.130
```

## Run

The following will build and deploy the default container stack locally:

```
# docker-compose up
```

Add the `-d` parameter to run in background.

This will run
* The [ApiLogicProject](ApiLogicProject) sqlite-backed northwind sample API
* Nginx reverse proxy

## Postgres

[docker-compose.nw_postgres.yml](docker-compose.nw_postgres.yml) Uses a postgres container instead of sqlite

```
docker-compose -f docker-compose.nw_postgres.yml up
```

This will run the code from [ApiLogicProject.postgres](ApiLogicProject.postgres)
