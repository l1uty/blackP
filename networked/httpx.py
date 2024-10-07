import requests

# 发送get请求
resp = requests.get(url='xxxxxx')
resp.encoding = 'utf-8'

# 发送post请求
data = {'uname':'test','pass':'test'}
resp = requests.post(url='xxxxxx',data=data)
print(resp.text)
print(resp.headers)

# 登录成功后获取响应的cookie,用于后续请求中响应,维持session
cookie = resp.cookies

# 下载图片
resp = requests.get(url='xxxxx')
with open('./test.png',mode='wb')as file:
    file.write(resp.content)

# 文件上传
file = {'batchfile':open('C:/tmp/sb.txt','rb')}
data = {'bathinfo':'gbk000300090'}
reps = requests.post(url='xxxxxxx',data=data,files=file,cookies=cookie)

# 第二种维持session的方法
session = requests.session()
data = {'uname':'test','pass':'test'}
resp = session.post(url='xxxxxxx',data=data)
file = {'batchfile':open('C:/tmp/sb.txt','rb')}
data = {'bathinfo':'gbk000300090'}
reps = session.post(url='xxxxxx',data=data,files=file,cookies=cookie)
