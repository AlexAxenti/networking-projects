import threading
import socket
from commands import commands

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

def handleClientMessage(client, message): 
  if message.startswith('/'):
    parts = message.split(' ')
    command = parts[0]

    if command in commands:
      argCount = len(commands[command]['arguments'])
      if (len(parts) - 1 < argCount):
        client.send(f'Incorrect arguments for {command}! Type "/help" for the list of commands.'.encode())
        return
      
      args = parts[1:]
      commands[command]['action'](args, client, nicknames, clients)
    else:
      client.send('Invalid command! Type "/help" for the list of commands.'.encode())
  else:
    clientIndex = clients.index(client)
    nickname = nicknames[clientIndex]
    broadcast(f"{nickname}: {message}")

def handle(client):
  while True:
    try:
      message = client.recv(1024)
      handleClientMessage(client, message.decode())
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

    isUnique = False
    nickname = ""
    while not isUnique:
      client.send('NICK'.encode())
      nickname = client.recv(1024).decode()
      if nickname in nicknames:
        client.send('Nickname is in use. Please choose another one'.encode())
      else:
        isUnique = True
        clients.append(client)
        nicknames.append(nickname)
        
    print(f"Nickname of the client is {nickname}")
    client.send('Connected to the server! Type "/help" for the list of commands!'.encode())
    broadcast(f"{nickname} has joined the chat!")


    thread = threading.Thread(target=handle, args=(client,))
    thread.start()

try:
  receive()
except KeyboardInterrupt:
  print("Server is shutting down...")
  server.close()