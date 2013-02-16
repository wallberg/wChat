wChat
=====

Ben and Micah learn some network programming

Server algorithm
----------------

<pre>
Determine which port to listen on (default is 99877)
Open server port for listening
stop-command-received = False
while ((new connection or dropped connection or new command) and !stop-command-received)
  if (new connecton)
    get user name
    store connection
  else if (dropped connection)
    remove stored connection
  else if (new message)
    if (command = stop)
      stop-command-received = True
    else if (command = message)
      foreach stored connection
        send message
close server port
</pre>
