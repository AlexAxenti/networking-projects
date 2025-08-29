import threading
import socket

HOST = '127.0.0.1'
PORT = 6000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server is listening at {HOST} port {PORT}")

clients = []
nicknames = []

def broadcast(message):
  for client in clients:
    client.send(message.encode())


def handle(client):
  while True:
    try:
      message = client.recv(1024)
      broadcast(message.decode())
    except:
      index = clients.index(client)
      clients.remove(client)
      client.close()
      nickname = nicknames[index]
      nicknames.remove(nickname)
      broadcast(f'{nickname} left the chat!')
      break

def receive():
  while True:
    client, address = server.accept()
    print(f"Connected with {str(address)}")

    client.send('NICK'.encode())
    nickname = client.recv(1024).decode()
    clients.append(client)
    nicknames.append(nickname)
        
    print(f"Nickname of the client is {nickname}")
    client.send('Connected to the server!'.encode())
    broadcast(f"{nickname} has joined the chat!")


    thread = threading.Thread(target=handle, args=(client,))
    thread.start()

try:
  receive()
except KeyboardInterrupt:
  print("Server is shutting down...")
  server.close()