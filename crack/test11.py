import requests
import time
def poc(url):
    poc_url = url + '/#/login?redirect=/dashboard'
    data = {
        'username': "xxx",
        'password': "xxx"
    }
    try:
        res = requests.post(poc_url, data=data, timeout=5)
        if (res.headers.get("Set-Cookie")):
            print(url + '/login.html')
    except BaseException:
        pass

if __name__ == '__main__':
    with open ('url.txt', 'r') as f:
        for i in f:
            poc(i.rsplit('\n'))
