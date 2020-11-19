import socket

sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_.connect((socket.gethostbyname(socket.gethostname()), 8888))
msg = sock_.recv(1024)
sock_.close()
print(msg.decode("ascii"))
