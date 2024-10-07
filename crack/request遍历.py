import json
import requests
import re

for i in range(0, 200):
    url = 'http://testphp.vulnweb.com/artists.php/update/' + str(i)
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10"
        "Cookie: PHPSESSID="
    }
    resp = requests.get(url, headers=head)
    result = resp.text
    obj = re.compile(r'用户名:</label>.*?value="(?P<name>.*?)"', re.S)
    rest = obj.finditer(result)
    for it in rest:
        a = it.group('name')
        print(a)