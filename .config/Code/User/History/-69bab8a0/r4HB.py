import socket

MAX_BYTES = 65535
port = 9000

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1' , port))
print('Listening at {}'.format(sock.getsockname))
while True:
    data,address =  sock.recvfrom(MAX_BYTES)
    text = data.decode('ascii')
    text = ('The client at {}says {!r}'.format(address,text))
    data = text.encode('ascii')
    sock.sendto(data,address)