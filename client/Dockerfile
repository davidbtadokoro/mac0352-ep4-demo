# Imagem base
FROM alpine:3.16

# Customizando o prompt
COPY ./client-profile /etc/profile
RUN apk add ncurses

# Resolvendo dependências
RUN apk add build-base

# Configurando e compilando inetutils-2.0 (incluindo ftp)
COPY ./inetutils-2.0 /usr/local/inetutils-2.0
WORKDIR /usr/local/inetutils-2.0
RUN ./configure && make clean && make

# Definindo diretório onde a demo ocorrerá
WORKDIR ./ftp
