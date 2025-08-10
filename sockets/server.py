import socket

host = '127.0.0.1'
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
conn, addr = s.accept()
while True:
    data = conn.recv(1024)
    if not data: 
        break
    conn.sendall(data)
conn.close()

