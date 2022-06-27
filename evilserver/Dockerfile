# Imagem base
FROM alpine:3.16

# Customizando o prompt
COPY ./evilserver-profile /etc/profile
RUN apk add ncurses

# Resolvendo dependências
RUN apk add --update python3 \
    && apk --update add py-pip \
    && pip install requests

# Transferindo código fonte do servidor malicioso
COPY ./evilserver.py /usr/local/

# Definindo diretório onde a demo ocorrerá
WORKDIR /usr/local/
