import os

def ping_ip():
    for i in range(1,255):
        ip = f'10.0.0.{i}'
        output = os.popen(f'ping -c 2 -w 1 {ip}').read()
        if 'ttl' in output:
            print(f'{ip} is online')

if __name__ == '__main__':
    ping_ip()