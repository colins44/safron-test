#client is also a socket
from socket import *


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket(AF_INET, SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
# s.send(MESSAGE)
while True:
    input = raw_input('enter a interger or a list of intergers seperated by a comma. eg: 2, 6: ')
    s.send(input)
    data = s.recv(BUFFER_SIZE)
    if data: print data
    continue
s.close()

print "received data:", data