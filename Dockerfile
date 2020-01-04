FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y python3-dev build-essential

ADD requirements.txt /app/
ADD ./app /app
ADD ./models /models

WORKDIR /app

RUN pip install -r requirements.txt
