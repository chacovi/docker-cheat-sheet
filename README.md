# Docker Cheat-Sheet

## Docker CLI

### List Docker CLI commands

> `$ docker`
>
> `$ docker [command] --help`

### Display Docker version and info

> `$ docker --version`
>
> `$ docker version`
>
> `$ docker info`

### Get Docker image

> `$ docker pull [image-name]`

### Execute Docker image (run, interactive, backgound)

> `$ docker run [image-name]`
>
> `$ docker run --name [container-name][image-name]`
>
> `$ docker run -it [image-name]`
>
> `$ docker run -dit [image-name]`

### Execute Docker image with volume

> `$ docker run -dit -v [local-path]:[container-path] [image-name]`

    For example:
    $ docker run -dit -v "$PWD":/home/app ubuntu

### Execute Docker image with port

> `$ docker run -p [local-port]:[container-port] [image-name]`

    For example:
    $ docker run -p 5001:5000 hello-world

### List Docker images

> `$ docker image ls`
>
> `$ docker images`

### List Docker containers (running, all, all in quiet mode)

> `$ docker container ls`
>
> `$ docker container ls --all`
>
> `$ docker container ls -aq`

### Exec command into Docker Container

> `$ docker exec -it [containerId] [command]`
>
> `$ docker exec -it [container-name] [command]`

    For example:
    $ docker exec -it 20d1c5cdbbd9 bash

## Docker Hub

### Login

> `$ docker login`

### Tag a release

> `$ docker tag image username/repository:tag`

    For example:
    $ docker tag friendlyhello gordon/get-started:part2
    $ docker tag apitax-docker-2.1.4 nopatience/middleware:2.1.4
    $ docker tag python-flask:latest chacovi/python-flask:1.0

### Push a release

> `$ docker push username/repository:tag`

    For example:
    $ docker push nopatience/middleware:2.1.4
    $ docker push chacovi/python-flask

### Pull a release and build - prioritizes local over pulling from docker hub

> `$ docker run -p 4000:80 username/repository:tag`

    For example:
    $ docker run -p 5080:80 nopatience/middleware:2.1.4

## Dockerfile

### Build Docker container using a dockerfile

> `$ docker build -t [image-name] [Dokerfile-path]`

    For example:
    $ docker build -t python-flask .
    $ docker run --name flask-demo -p 5000:5000 python-flask

## Docker-compose

### Build containers using a docker-compose file

> `$ docker-compose rm`
>
> `$ docker-compose up -d`

## Docker-machine

### Create a docker machine for vbox

> `$ docker-machine create --driver=virtualbox vbox-default`
>
> `$ docker-machine env vbox-default`
>
> `$ docker-machine ls`

## Kubernates

### Create a kubernate

> `$ minikube start`
>
> `$ kubectl run nginx --image=nginx`
>
> `$ kubectl get pods`
>
> `$ kubectl get deployments`
