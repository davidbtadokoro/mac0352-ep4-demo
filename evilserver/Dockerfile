# Imagem base
FROM alpine:3.16

# Customizando o prompt
COPY ./evilserver-profile /etc/profile
RUN apk add ncurses

# Resolvendo dependências
RUN apk add --update python3 \
    && apk --update add py-pip \
    && pip install requests

# Criando o diretório que terá o código malicioso
RUN mkdir /usr/local/malicious-code

# Definindo diretório onde a demo ocorrerá
WORKDIR /usr/local/malicious-code
