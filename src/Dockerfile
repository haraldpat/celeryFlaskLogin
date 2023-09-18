FROM spotmentor/alpine-protobuf:1.0.0

RUN apk add --no-cache --virtual .build-deps build-base

ENV PYTHONUNBUFFERED 1

ENV LIBRARY_PATH=/lib:/usr/lib

RUN mkdir /src

WORKDIR /src

ADD requirements.txt /src/

RUN pip install --upgrade pip

COPY requirements.txt /
RUN pip install -r requirements.txt && apk del .build-deps

ADD . /src
