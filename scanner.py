#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid systax")
    sys.exit()

print('.' * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print('.' * 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        print(f"Checking port {port}")
        if result == 0:
            print(f'Port {port} is open')
        s.close()
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()

except socket.gaierror:
    print("\n Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\nCouldn't Conneto to server.")
    sys.exit()