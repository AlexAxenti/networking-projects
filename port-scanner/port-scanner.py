import socket
import sys

target_host = -1
target_port = -1
from_port_range = 1
to_port_range = 65535

def initialize_agruments():
  global target_host
  global target_port
  global from_port_range
  global to_port_range

  if len(sys.argv) >= 2:
    target_host = socket.gethostbyname(sys.argv[1])

    if len(sys.argv) == 3:
      target_port = int(sys.argv[2]) 
    elif len(sys.argv) == 4:
      from_port_range = int(sys.argv[2])
      to_port_range = int(sys.argv[3])
  else:
    print("Incorrect number of arguments - Usages:\n" \
    "port-scanner.py <host>\n" \
    "port-scanner.py <host> <port>\n" \
    "port-scanner.py <host> <from-port-range> <to-port-range>\n")
    exit()

def scan_port(host, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(1)
  try:
    result = s.connect_ex((target_host, port))
    return result
  finally:
    s.close()

def execute_scan():
  if target_port == -1:
    for port in range(from_port_range, to_port_range+1):
      result = scan_port(target_host, port)
      if result == 0:
        print(f"Port {port} is open")
      else:
        print(f"Port {port} is closed")
  else:
    result = scan_port(target_host, target_port)
    if result == 0:
      print(f"Port {target_port} is open")
    else:
      print(f"Port {target_port} is closed")

initialize_agruments()
execute_scan()
