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

The following will build and deploy the container locally.

```
# docker-compose up
```

Add the `-d` parameter to run in background.


