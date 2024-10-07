import collections

import requests
import urllib.parse
from termcolor import colored

# 检查是否安装了 termcolor 模块
try:
    from termcolor import colored
except ImportError:
    print("[!] 'termcolor' 模块未找到，请运行以下命令进行安装：\n    pip install termcolor")
    exit(1)

# 目标 URL
目标网址 = "http://....."

# 美化输出
横幅 = """
------------------------------------------------
       本地文件包含 (LFI) 测试工具
------------------------------------------------
"""

print(colored(横幅, "cyan"))


# 通过请求测试文件路径
def lfi(文件路径):
    文件编码 = urllib.parse.quote(文件路径)
    url = f"{目标网址}{文件编码}"

    print(colored(f"[+] 正在测试文件：{文件路径}", "blue"))
    try:
        响应 = requests.get(url)
        if 响应.status_code == 200 and len(响应.text) > 0:
            print(colored(f"[+] 文件内容：\n", "green") + 响应.text)
        else:
            print(colored("[!] 文件不可读或为空", "red"))
    except requests.exceptions.RequestException as e:
        print(colored(f"[!] 请求失败：{e}", "red"))
    print("\n" + "-" * 50 + "\n")
    print("可以检查一下路径是否正确，并确定一下文件是否存在损坏")

def main():
    while True:
        文件路径 = input(colored("[+] 请输入文件路径（输入 'exit' 退出）：", "blue"))
        if 文件路径.lower() == 'exit':
            print(colored("[!] 退出工具", "yellow"))
            break
        lfi(文件路径)

def liuty():
    while True:
        文件路径 = input(colored(""))

if __name__ == "__main__":
    main()
