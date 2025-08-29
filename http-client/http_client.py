import json, socket

def get():
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    client.connect(('127.0.0.1', 8000))
    client.sendall((
      "GET / HTTP/1.1\r\n" \
      "Host: localhost:8000\r\n" \
      "Connection: close \r\n"
      "\r\n"
    ).encode())

    chunks = []
    while True:
      data = client.recv(4096)
      if not data:
        break
      chunks.append(data)

    resp_bytes = b"".join(chunks)
    print(f'Received {resp_bytes.decode()}')
  finally:
    client.close()

def post():
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  payload = {"name": "alex", "course": "networking"}
  body = json.dumps(payload).encode()

  try:
    client.connect(('httpbin.org', 80))

    req = (
      "POST /post HTTP/1.1\r\n" \
      "Host: httpbin.org\r\n" \
      "Connection: close \r\n"
      "Content-Type: application/json\r\n"
      f"Content-Length: {len(body)}\r\n"
      "\r\n"
    ).encode() + body

    client.sendall(req)

    chunks = []
    while True:
      data = client.recv(4096)
      if not data:
        break
      chunks.append(data)

    resp_bytes = b"".join(chunks)
    print(f'Received {resp_bytes.decode()}')
  finally:
    client.close()
  print()

# get()
# post()