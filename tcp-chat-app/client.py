import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 6000))

# ANSI escape codes for colors and reset
# BLACK = '\033[0;30m'
# RED = '\033[0;31m'
# GREEN = '\033[0;32m'
# YELLOW = '\033[0;33m'
# BLUE = '\033[0;34m'
# MAGENTA = '\033[0;35m'
# CYAN = '\033[0;36m'
# WHITE = '\033[0;37m'
# RESET = '\033[0;0m'

def receive():
  while True:
    try:
      message = client.recv(1024).decode()
      if message == 'NICK':
        client.send(input("Choose a nickname: ").encode())
      else:
        print(message)
    except Exception as e:
      print(f'An error occurred: {e}')
      client.close()
      break

def write():
  while True:
    message = f'{input("")}'
    client.send(message.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()