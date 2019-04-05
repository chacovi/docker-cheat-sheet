FROM python:3.6-slim

RUN pip install Flask redis

WORKDIR /app

COPY ./app.py /app

EXPOSE 5000

CMD [ "python","app.py" ]