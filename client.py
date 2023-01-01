import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(b'Hello, friend!', ('127.0.0.1', 8888))

