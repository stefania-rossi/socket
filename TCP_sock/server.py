import socket

IP = '127.0.0.1'
PORTA = 65432
DIM_BUFFER = 1024 

# Creazione socket del server con costrutto with
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:

  # Binding della socket della porta specificata
  sock_server.bind((IP, PORTA))

  # Mette socket in ascolto per connessioni in ingresso
  sock_server.listen()

  print(f"Server in ascolto su {IP}:{PORTA}...")

  # Loop principale del server
  while True:
    # accetta le connessioni
    sock_service, address_client = sock_server.accept()
    with sock_service as sock_client:
      # leggi i dati inviati dal client
      dati = sock_client.recv(DIM_BUFFER).decode()

      # Stampa il messaggio ricevuto e invia risposta al client
      print(f"Ricevuto messaggio dal client {sock_client}:{dati}")
      sock_client.sendall("Messaggio ricevuto dal server".encode())