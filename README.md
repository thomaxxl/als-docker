# ApiLogicProject using Docker and docker-compose

## Installation

```
# git clone https://github.com/thomaxxl/als-docker
# cd als-docker
```

## Configure

To configure the ApiLogicProject, change the environement variables in [docker_compose.yml](docker_compose.yml):
```
    api-logic-server:
        environment:
          - SWAGGER_HOST=192.168.109.130
          - FLASK_HOST=0.0.0.0
          - PORT=80
```

## Run

The following will build and deploy the container locally.

```
# docker-compose up
```

Add the `-d` parameter to run in background.


