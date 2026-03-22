import socket

HOST = '127.0.0.1' 
PORT = 65432 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
  sock_service.connect((HOST, PORT))
  sock_service.sendall(b'Hello, world') 
  data = sock_service.recv(1024) 

print('Received', data.decode())