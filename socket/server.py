import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    while True:
        msg = input("input: ")
        clientsocket.send(bytes(msg,"utf-8"))
        receive = clientsocket.recv(1024).decode("utf-8")
        print("CLIENT: ", receive)
    
