import socket
import json


SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((SERVER_IP, SERVER_PORT))

print("Server in attessa di messaggi...")

while True:

  data, addr = s.recvfrom(BUFFER_SIZE)
  if not data:
    break
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
  s.sendto(str(reply).encode("UTF-8"), addr)