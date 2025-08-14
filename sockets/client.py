import socket

# Адрес и порт сервера, к которому будет выполняться подключение
server_host = '127.0.0.1'
server_port = 8888

# Создаем сокет, протоколы IP и TCP
s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM)
# Подключаемся к серверу
s.connect((server_host, server_port))
# Отправляем данные на сервер
s.sendall(b'Hello, world!')
# Получаем данные от сервера
data = s.recv(1024)
# Закрываем сокет
s.close()
# Печатаем данные, которые получили от сервера
print('Полученные данные:', data)
