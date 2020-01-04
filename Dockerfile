FROM python:3.8-slim-buster

ADD requirements.txt /app/

RUN apt-get update && apt-get install -y python3-dev build-essential && pip install -r /app/requirements.txt
