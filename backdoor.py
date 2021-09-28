import os, platform, socket

ip_add = ""
port = 6666  # listening port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding to NIC
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((ip_add, port))

s.listen(1)

connection, address = s.accept()

while True:
    try:
        opt = connection.recv(1024)
    except:
        continue

    # Send Platform info
    if (opt.decode("utf-8") == "1"):
        info = platform.platform() + " " + platform.machine()
        connection.sendall(info.encode())
    
    # Send list of requested path
    elif (opt.decode("utf-8") == "2"):
        path = connection.recv(1024)

        try:
            dir_lst = os.listdir(path.decode("utf-8"))
            info = ", ".join(dir_lst)
            
        except:
            info = "Wrong path!"

        connection.sendall(info.encode())
        
    # Close connection
    elif (opt.decode("utf-8") == "0"):
        connection.close()
        connection, address = s.accept()
