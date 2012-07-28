#!/usr/bin/env python
import socket

class wChatClient:
   host = '127.0.0.1'
   port = 45575

   def __init__(self, host, port):
      self.host = host
      self.port = port

   def run(self):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

      print 'Connecting to (%s,%s)' % (self.host, self.port)
      s.connect((self.host, self.port))

      m = 'Hello, World!'
      print 'Sending: ', m
      s.sendall(m)

      data = s.recv(1024)
      print 'Received: ', repr(data)

      print 'Closing connection to (%s,%s)' % (self.host, self.port)
      s.close()

s = wChatClient('127.0.0.1',45575)
s.run()
