# -*- coding: utf-8 -*-
"""

@author: war19
"""

import socket

s=socket.socket()
print("socket created")

s.bind(('localhost',9997))
s.listen(3)
print("waiting for connection")

while True:
    c,addr=s.accept()
    name=c.recv(1024).decode()
    print("connected with",addr,name)
    
    c.send(bytes('hey wilcome to harsh','utf-8'))
    c.close()

    