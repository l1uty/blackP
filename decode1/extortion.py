# 针对某个文件进行base64转码并加密并保存
import base64
import os

def encrypt(filepath):
    with open(filepath, mode='rb') as file:
        data = file.read()

    source = base64.b64encode(data).decode()
    dest = ''
    for c in source:
        dest += chr(ord(c)+5)
    with open(filepath + '.enc', mode='w') as file:
        file.write(dest)
    os.remove(filepath)

# 解密
def decrypt(filepath):
    with open(filepath, mode='r') as file:
        content = file.read()
    dest = ''
    for c in content:
        dest += chr(ord(c)-5)

    newfile = filepath.replace('.enc', '')
    with open(newfile, mode='wb') as file:
        file.write(base64.b64decode(dest))

    os.remove(filepath)

if __name__ == '__main__':
    decrypt('./test.png.enc')
