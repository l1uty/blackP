from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex

# 加密
source = 'Hello你好'

# 如果source分组后剩余长度不足16位的倍数就用空格补足为16位
if len(source.encode('utf-8')) % 16:
    add = 16 - (len(source.encode('utf-8')) % 16)
else:
    add = 0
source = source + ('\0' * add)
print(source)

# 定义密钥和偏移量，必须是16个字节、24个字节或32个字节
key = 'todayiswonderful-abcdef123456789'.encode()
mode = AES.MODE_CBC
iv = b'9876543210FEDCBA'
cryptos = AES.new(key, mode, iv)

cipher = cryptos.encrypt(source.encode())
print(cipher)
print(b2a_hex(cipher).decode())

# 解密
source = '上面加密完的结果'
key = 'todayiswonderful-abcdef123456789'.encode()
mode = AES.MODE_CBC
iv = b'9876543210FEDCBA'
cryptos = AES.new(key, mode, iv)

dest = cryptos.decrypt(a2b_hex(source))
print(dest.decode().rstrip('\0'))