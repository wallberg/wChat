#!/usr/bin/env python
import socket

class wChatServer:
   host = ''
   port = 45575

   def __init__(self, host, port):
      self.host = host
      self.port = port

   def run(self):

      # open host,port for listening
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.bind((self.host, self.port))
      s.listen(1)
      conn, addr = s.accept()
      print 'Connected by', addr
      while 1:
         data = conn.recv(1024)
         if not data: break
         conn.send(data)
      conn.close()

s = wChatServer('',45575)
s.run()
