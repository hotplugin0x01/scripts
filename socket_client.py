#!/bin/python3

import sys
import socket

if len(sys.argv) < 3:
    print("Invalid Arguments!")
    print("Syntax: python3 socket_server.py <ip address> <port>")
    sys.exit()

else:
    ip_addr = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_addr, port))

    print("--- Connection established! ---")

    while True:
        message = input("\nEnter the message you want to send: ")
        s.sendall(message.encode())
        flag = s.recv(1024)
        print(flag.decode("utf-8"))
        s.close()
        break
