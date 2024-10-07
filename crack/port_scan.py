import socket
import threading
import time

# 端口扫描
def socket_port(IP):
    for port in range(1, 65535):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((IP, port))
            print(f"端口:{port}可用.")
        except ConnectionResetError:
            pass
        except socket.timeout:
            pass
        finally:
            s.close()

# 基于多线程的端口扫描
def threading_port(IP, start):
    for port in range(start, start + 50):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((IP, port))
            print(f"端口:{port}可用.")
        except:
            pass
        time.sleep(3)


if __name__ == "__main__":
    # socket_port('192.168.1.1')
    for port in range(1, 1000, 50):
        threading.Thread(target=threading_port, args=('117.78.49.99', port)).start()