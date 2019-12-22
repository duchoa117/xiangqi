import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    new_msg = True
    while True:
        msg = s.recv(1024).decode("utf-8")
        if new_msg:
            new_msg = False
        print("SERVER: ", msg)
        new_msg = True
        full_msg = ""
        send_msg = input("input: ").encode("utf-8")
        s.send(send_msg)