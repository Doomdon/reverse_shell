import socket


#s.send(b'Hello, friend')
#s.close()

while 1:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 8888))
        answer = input('Введите ваше сообщение: ')
    except KeyboardInterrupt:
        s.close()
        break
    else:
        s.send(answer.encode())

