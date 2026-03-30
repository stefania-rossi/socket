import socket
import json
from threading import Thread

def ricevi_comandi(sock_service, address_client):
    print(f"Thread create per ip: {address_client}")
    with sock_service as sock_client:
        data = sock_client.recv(DIM_BUFFER)
        if not data:
            return
        data = data.decode()
        data = json.loads(data)
        primoNumero = data["primoNumero"]
        operazione = data["operazione"]
        secondoNumero = data["secondoNumero"]
        if operazione == "+":
            r = primoNumero+secondoNumero
        elif operazione == "-":
            r = primoNumero-secondoNumero
        elif operazione == "*":
            r = primoNumero*secondoNumero
        elif operazione == "/":
            r = primoNumero/secondoNumero
        else:
            r = "Operatore non valido!"

        reply = r
        sock_client.sendall(str(reply).encode())
    
    
def ricevi_connessioni(sock_listen):
    sock_service,address_client = sock_listen.accept()
    try:
        Thread(target=ricevi_comandi, args=(sock_service, address_client)).start()
    except Exception as e:
        print(e)

def avvia_server(indirizzo,porta):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
        sock_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

        sock_server.bind((indirizzo,porta))

        sock_server.listen(5)

        print(f" ---- Server in ascolto su {indirizzo}:{porta} ---- ")
        while True:
            ricevi_connessioni(sock_server)
            

IP = "127.0.0.1"
PORTA = 22224
DIM_BUFFER = 1024

avvia_server(IP,PORTA)