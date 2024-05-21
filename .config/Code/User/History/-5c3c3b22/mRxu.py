import socket
from datetime import datetime
import random

MAX_BYTES = 65535
port = 9000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 9001))  
data, address = sock.recvfrom(MAX_BYTES)
text = data.decode('ascii')
print('Received message from client:', text)

