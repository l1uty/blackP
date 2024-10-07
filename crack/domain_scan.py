import os
import socket
import threading

def ping_domain():
    with open('./dict.txt') as file:
        domain_list = file.readlines()
    for domain in domain_list:
        result = os.popen(f"ping -c 2 -w 1 {domain.strip()}.xxx.com").read()
        if 'ttl' in result:
            print(f"{domain.strip()}.xxx.com")

def socket_domain():
    with open('./dict.txt') as file:
        domain_list = file.readlines()
    for domain in domain_list:
        try:
            ip = socket.gethostbyname(f'{domain.strip()}.meddigi.htb')
            print(f'{domain.strip()}.meddigi.htb, {ip}, ')
        except:
            pass

if __name__ == '__main__':
    # ping_domain()
    with open('./dict.txt') as file:
        domain_list = file.readlines()
    for i in range(0, len(domain_list), 500):
        sublist = domain_list[i:i+100]
        threading.Thread(target=socket_domain(), args=(sublist, )).start()
