import socket 
import json

HOST = '127.0.0.1' 
PORT = 65432 


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((HOST, PORT))

    primoNumero = float(input("Inserisci il primo numero: "))
    operazione = input("Inserisci l'operazione (simbolo)")
    secondoNumero = float(input("Inserisci il secondo numero: "))
    messaggio = {"primoNumero":primoNumero,
                "operazione":operazione,
                "secondoNumero":secondoNumero
                }
    messaggio = json.dumps(messaggio)
    sock_service.sendall(messaggio.encode())
    print(f"Messaggio inviato al server: {messaggio}")

  
    data = sock_service.recv(1024)
    print(f"Messaggio ricevuto dal server : {data.decode()}")

