# WIP

def listClients(client, nicknames):
  clientList = ', '.join(nicknames)
  client.send(f"Connected clients: {clientList}".encode())

def sendMessage(targetNickname, message, client, nicknames, clients):
  if targetNickname in nicknames:
    targetIndex = nicknames.index(targetNickname)
    targetClient = clients[targetIndex]
    targetClient.send(f"Message from {nicknames[clients.index(client)]}: {message}".encode())
  else:
    client.send(f"User {targetNickname} not found.".encode())

def showHelp(client):
  helpMessage = 'Available Commands:\n'
  for command in commands:
    helpMessage += f"{command}"
    for arg in commands[command]['arguments']:
      helpMessage += f" <{arg}>"
    helpMessage += "\n"
  client.send(helpMessage.encode())

commands = {
  '/list': {'arguments': [], 'action': lambda args, client, nicknames, clients: listClients(client, nicknames)},
  '/msg': {'arguments': ['nickname', 'message'], 'action': lambda args, client, nicknames, clients: sendMessage(args[0], ', '.join(args[1:]), client, nicknames, clients)},
  '/help': {'arguments': [], 'action': lambda args, client, nicknames, clients: showHelp(client)}
}
  
  