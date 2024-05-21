import socket
from datetime import datetime
import random
MAX_BYTES = 65535
port = 9000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
request_id = random.randint(1, 10000)
text = 'The time is {} (Request ID: {})'.format(datetime.now(), request_id)
data = text.encode('ascii')
sock.sendto(data, ('127.0.0.1', port))
print('The OS assigned me the address {}'.format(sock.getsockname()))
data, address = sock.recvfrom(MAX_BYTES)
text = data.decode('ascii')
response_id = int(text.split(' (Request ID: ')[1].split(')')[0])
if request_id == response_id:
    print ('The server {} replied {!r}'.format(address,text))
else:
    print('Invalid request ID received. Potential attack detected!')
