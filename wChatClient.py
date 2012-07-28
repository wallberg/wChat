#!/usr/bin/env python
import socket

class wChatClient:
   host = ''
   port = 45575

   def __init__(self, host, port):
      self.host = host
      self.port = port

   def run(self):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((self.host, self.port))
      s.sendall('Hello, world')
      data = s.recv(1024)
      s.close()
      print 'Received', repr(data)

s = wChatClient('',45575)
s.run()
