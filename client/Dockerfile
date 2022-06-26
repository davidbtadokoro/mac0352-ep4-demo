FROM alpine:3.16

RUN apk add build-base

COPY ./inetutils-2.0 /usr/local/inetutils-2.0

WORKDIR /usr/local/inetutils-2.0

RUN ./configure && make clean && make

WORKDIR ./ftp
