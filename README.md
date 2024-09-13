## validate or test compose file before up

```
 docker compose config
```

## start compose

```
docker compose up -d
```

## down compose

```
docker compose down
```

## docker log

```
docker logs -f <container>
```

## docker compose log

```
docker compose logs -f fastapi
 f means  Follow the log output
```

## docker build rebuild the image

```
docker compose up -d --build
```

## inside docker

```
docker exec -it myapi-fastapi-1 /bin/sh
ls
poetry show
exit
```
