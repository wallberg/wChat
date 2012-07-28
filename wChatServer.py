#!/usr/bin/env python
import socket

class wChatServer:
   host = '127.0.0.1'
   port = 45575

   def __init__(self, host, port):
      self.host = host
      self.port = port

   def run(self):

      # open host,port for listening
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.bind((self.host, self.port))
      s.listen(1)
      print 'Listening on (%s,%s) for a connection' % (self.host, self.port)

      conn, addr = s.accept()
      print 'Connection from', addr
      while 1:
         data = conn.recv(1024)
         if not data: break
         conn.send(data)

      conn.close()
      print 'Closed (%s,%s) for listening' % (self.host, self.port)

s = wChatServer('127.0.0.1',45575)
s.run()
