import time
import paramiko

def ssh():
    transport = paramiko.Transport(('192.168.31.169', 22))
    transport.connect(username='kali', password='kali')

    ssh = paramiko.SSHClient()
    ssh._transport = transport
    sftp = paramiko.SFTPClient.from_transport(transport)

    # 执行命令并获取结果
    stdin, statt, sttaar = ssh.exec_command('ls /tmp')
    print(statt.read().decode())
    time.sleep(2)
    stdin, statt, sttaar = ssh.exec_command('ifconfig')
    print(statt.read().decode()) 
    print()
    # 传输文件
    sftp.put('./test.png', '/tmp/test.png')
    sftp.get('/tmp/test.png', './test.png')
# redis
import socket

def redis123():
    s = socket.socket()
    s.connect(('xxx.xxx.xxx.xxx', 6379))
    s.send('*2\r\n$4\r\nauth\r\n$6\r\n123456\r\n'.encode())
    time.sleep(1)
    s.send('*3\r\n$3\r\nset\r\n$4\r\nname\r\n$4\r\nzhyf\r\n'.encode())
    time.sleep(1)
    s.send('*2\r\n$3\r\nget\r\nname\r\n'.encode())
    reply = s.recv(1024)
    print(reply.decode())

# 简单点，可以直接调用redis方法库
import redis
red = redis.Redis(host='xxx.xxx.xxx.xxx', port=6379, password='123456', db=0)
red.set('addr', 'chengdu')
print(red.get('addr').decode())
red.rpush('students', 'zhangsan')
red.rpush('students', 'lisi')
red.rpush('students', 'wangwu')


if __name__ == '__main__':
    redis123()
