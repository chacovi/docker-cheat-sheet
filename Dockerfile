#FROM ubuntu

#RUN apt-get update && apt-get install -y git

#WORKDIR /app

#COPY datos.txt /app

#CMD [ "echo","Hola" ]

FROM python:3.6-slim

RUN pip install Flask

WORKDIR /app

COPY app.py /app

EXPOSE 5000

CMD [ "python","app.py" ]