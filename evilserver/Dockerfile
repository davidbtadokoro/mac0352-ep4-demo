FROM alpine:3.16

RUN apk add --update python3 \
    && apk --update add py-pip \
    && pip install requests

COPY ./evilserver.py /usr/local/

WORKDIR /usr/local/
