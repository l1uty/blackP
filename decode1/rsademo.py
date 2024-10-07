import rsa
from binascii import b2a_hex,a2b_hex

# 生成公钥和私钥
pub, priv = rsa.newkeys(256)
print(pub, priv)

# 公钥加密
encrypt = rsa.encrypt('你好liuty'.encode(), pub)
print(encrypt)
print(b2a_hex(encrypt).decode())
enstr = b2a_hex(encrypt).decode()
print(enstr)

# 私钥解密
decrypt = rsa.decrypt(encrypt, priv)
print(decrypt.decode())
decrypt = rsa.decrypt(a2b_hex(enstr), priv)
print(decrypt.decode())