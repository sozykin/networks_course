import socket

server_host = '127.0.0.1'
server_port = 8888

s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM)

s.connect((server_host, server_port))
s.sendall(b'Hello, world!')
data = s.recv(1024)
s.close()
print('Полученные данные:', repr(data))
