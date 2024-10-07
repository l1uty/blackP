from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import ARP

def scapy_ip():
    for i in range(1, 255):
        ip = f'192.168.31.{1}'
        try:
            pkg = ARP(psrc='192.168.31.1', pdst=ip)
            reply = sr1(pkg, timeout=3, verbose=False)
            print(reply[ARP].hwsrc)
            print(f"{ip}在线")
        except:
            pass
def scapy_port(ip):
    for port in range(20, 8090):
        pkg = IP(src='192.168.31.1', dest=ip)/TCP(dport=port, flags='s')
        reply = sr1(pkg, timeout=3, verbose=False)
        if reply[TCP].flags == 0x12:
            print(f'端口{port}开放')


if __name__ == '__main__':
    # scapy_ip()
    scapy_port('192.168.31.1')