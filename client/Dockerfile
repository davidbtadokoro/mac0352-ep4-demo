# Imagem base
FROM alpine:3.16

# Customizando o prompt
COPY ./client-profile /etc/profile
RUN apk add ncurses

# Resolvendo dependências
RUN apk add build-base

# Configurando e compilando inetutils-2.1 (incluindo ftp)
COPY ./inetutils-2.1 /usr/local/inetutils-2.1
WORKDIR /usr/local/inetutils-2.1
RUN ./configure && make clean && make

# Configurando e compilando inetutils-2.1 (incluindo ftp)
COPY ./inetutils-2.2 /usr/local/inetutils-2.2
WORKDIR /usr/local/inetutils-2.2
RUN ./configure && make clean && make

# Definindo diretório onde a demo ocorrerá
WORKDIR /usr/local
