# 简单的可逆算法（只针对ASCII码）：
# 加密过程：大写变小写，小写变大写，数字+1
# 解密过程：大写变小写，小写变大写，数字-1
source = 'helloworld123'
dest = ''
for c in source:
# 大小写互转对于加解密本质是一样的
    if ord(c) in range(65, 91):
        temp = chr(ord(c)+32)
    elif ord(c) in range(97, 123):
        temp = chr(ord(c)-32)
    elif ord(c) in range(48, 58):
        temp = chr(ord(c)-1)
    dest += temp
print(dest)

# 凯撒加密,右移5位
list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for c in list:
    index = (list.index(c) + 5) % len(list)
    print(list[index], end=' ')
# 解密凯撒密码，左移5位
list2 = ['F', 'G', 'A', 'B', 'C', 'D', 'E']
for c in list2:
    index = list2.index(c) - 5
    print(list2[index], end=' ')

# 综合练习
import string

upper_list = string.ascii_uppercase
lower_list = string.ascii_lowercase

def zhangsan(source):
    dest = ''
    for c in source:
        if c in upper_list:
            index = (upper_list.index(c) + 5) % 26
            dest += upper_list[index]
        elif c in lower_list:
            index = (lower_list.index(c) + 5) % 26
            dest += lower_list[index]
    return dest

def lisi(source):
    dest = ''
    for c in source:
        if ord(c) >= 65 and ord(c) <= 90:
            dest += chr(ord(c) + 32)
        elif ord(c) >= 97 and ord(c) <= 122:
            dest += chr(ord(c) - 32)
    return dest

def wangwu(source):
    dest = ''
    for c in source:
        if c in upper_list:
            index = (upper_list.index(c) - 5)
            dest += upper_list[index]
        elif c in lower_list:
            index = (lower_list.index(c) - 5)
            dest += lower_list[index]
    return dest


if __name__ == '__main__':
    result1 = zhangsan('LiutyNB')
    print(result1)
    result2 = lisi(result1)
    print(result2)
    result3 = wangwu(result2)
    print(result3)