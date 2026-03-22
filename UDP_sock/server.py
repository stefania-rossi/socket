import socket 

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005
BUFFER_SIZE = 1024
NUM_MESSAGES = 5

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(NUM_MESSAGES):
    message = "ping"
    sock.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
    print(f"Messaggio inviato al server: {message}")

    data, addr = sock.recvfrom(BUFFER_SIZE)
    print(f"Messaggio ricevuto dal server {addr}: {data.decode()}")

sock.close()