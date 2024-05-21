import random,socket

MAX_BYTES = 65535
port = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', port))  
print('Listening at{}'.format(sock.getsockname()))

while True:
    data, address = sock.recvfrom(MAX_BYTES)
    if random.random()<0.5:
        print('Pretending to drop packet from{}'.format(address))
        continue
text = data.decode('ascii')
print('The client at{} says{!r}'.format(address, text))
message='your data was{} bytes long'.format(len(data))
sock.sendto(message.encode('ascii'),address)