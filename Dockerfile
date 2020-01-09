FROM python:3.8-slim-buster

ADD requirements.txt /app/

RUN apt-get update \
    && apt-get install -y mecab \
    && apt-get install -y libmecab-dev \
    && apt-get install -y mecab-ipadic-utf8 \
    && apt-get install -y git \
    && apt-get install -y make \
    && apt-get install -y curl \
    && apt-get install -y xz-utils \
    && apt-get install -y file \
    && apt-get install -y sudo \
    && apt-get install -y wget \
    && apt-get install -y python3-dev build-essential \
    && pip install -r /app/requirements.txt

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
    && cd mecab-ipadic-neologd \
    && bin/install-mecab-ipadic-neologd -n -y --prefix /usr/local/lib/mecab/dic/mecab-ipadic-neologd
