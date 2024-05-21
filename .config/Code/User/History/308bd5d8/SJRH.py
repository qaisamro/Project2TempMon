import socket
from datetime import datetime

MAX_BYTES = 65535
port = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
text = 'The time is {}'.format(datetime.now())
data = text.encode('ascii')
sock.sendto(data,('127.0.0.1',port))
print('The OS  assigned me the address{}'.format(sock.getsockname()))
data,address = sock.recvfrom(MAX_BYTES)
text = data.decode('ascii')
print ('The server {} replied {!r}'.format(address,text))
