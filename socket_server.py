#!/bin/python3

import socket
import sys

if len(sys.argv) < 3:
    print("Invalid Arguments!")
    print("Syntax: python3 socket_server.py <ip address> <port>")
    sys.exit()

else:
    ip_addr = sys.argv[1]
    port = int(sys.argv[2])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip_addr, port))
    sock.listen(1)

    print("-" * 50)
    print("Server started. Waiting for connection...")
    print("-" * 50)

    connection, ip = sock.accept()
    print(f"\nClient connected with address: {ip}")

    while True:
        data = connection.recv(1024)
    
        if not data: 
            break
    
        connection.sendall(b"\n-----Message Received-----")
    
        print("\n", data.decode("utf-8"))

    connection.close()