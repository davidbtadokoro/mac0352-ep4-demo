# CRIANDO AS IMAGENS E EXECUTANDO OS CONTÂINERS

## Criação das imagens e execução dos contâiners:
docker system prune -a \
&& docker-compose build --no-cache \
&& docker-compose up

## Entrando nos contâiners:
docker exec -it evilserver /bin/sh
docker exec -it client /bin/sh
docker exec -it internalservice /bin/sh

## Preparando o prompt:
source /etc/profile && clear
------------------------------------------------
------------------------------------------------

# DEMONSTRANDO O ATAQUE

## Cliente:
./ftp --version
./ftp evilserver -p

## Servidor Malicioso:
python3 evilserver.py

## Serviço Interno:
nc -lnvp 22
------------------------------------------------
------------------------------------------------

# DEMONSTRANDO O PATCH

# Cliente:
cd ../inetutils-2.2 \
&& ./ftp evilserver -p

# Servidor Malicioso:
python3 evilserver.py

# Serviço Interno:
nc -lnvp 22
------------------------------------------------
------------------------------------------------
