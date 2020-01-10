FROM python:3.8-slim-buster

COPY requirements.txt /app/

RUN apt-get update \
    && apt-get install -y --no-install-recommends mecab \
    && apt-get install -y --no-install-recommends libmecab-dev \
    && apt-get install -y --no-install-recommends mecab-ipadic-utf8 \
    && apt-get install -y --no-install-recommends git \
    && apt-get install -y --no-install-recommends make \
    && apt-get install -y --no-install-recommends curl \
    && apt-get install -y --no-install-recommends xz-utils \
    && apt-get install -y --no-install-recommends file \
    && apt-get install -y --no-install-recommends sudo \
    && apt-get install -y --no-install-recommends wget \
    && apt-get install -y --no-install-recommends python3-dev build-essential \
    && pip install -r /app/requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
    && /mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y --prefix /usr/local/lib/mecab/dic/mecab-ipadic-neologd
