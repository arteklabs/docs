[![Docker Image CICD](https://github.com/arteklabs/docs/actions/workflows/dockerhub.yml/badge.svg)](https://github.com/arteklabs/docs/actions/workflows/dockerhub.yml)

# Getting Started

To run this app, create a file `compose.yaml` with the following content:

```
version: '3'
services:
  redis:
    image: redis
    container_name: redis.dditreduk
    networks:
      - network.dditreduk
    ports:
      - "6379:6379"
  app:
    image: dditreduk/nnrco:latest
    container_name: app.dditreduk
    networks:
      - network.dditreduk
    depends_on:
      - redis

networks:
  network.dditreduk:
    name: network.dditreduk
```

Run the app with:

```
$ docker-compose up -d
$ alias red="docker run -it --rm dditreduk/nnrco:latest python app.py"
$ red add --key tst --value tst
added (tst, tst)
$ docker exec -it redis.dditreduk redis-cli

127.0.0.1:6379> KEYS *
1) "tst"
```
# Clear resources

```
$ docker-compose down --remove-orphans
$ docker-compose down --rmi all
```
