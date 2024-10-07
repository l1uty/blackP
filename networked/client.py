import socket

s = socket.socket()
s.connect(('127.0.0.1',5555))

while True:
    message = input("请输入消息：")
    s.send(message.encode())
    receive = s.recv(10240)
    print(f"ccc回复：{receive.decode()}")
