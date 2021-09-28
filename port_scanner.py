#!/bin/python3

import sys
import socket
from datetime import datetime

# Defining Target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])   # Resolve hostname to IP
else:
    print("Invalid arguments!")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        # print(f"Checking Port {port}")
        result = s.connect_ex((target, port))   # returns an error indicator
        if result == 0:
            print(f"Port {port} is open.")
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to the server.")
    sys.exit()