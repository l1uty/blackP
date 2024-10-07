import re,requests
import random
import time

# 解析网页所有超链接
res = requests.get('http://xxxxxx')

def spider_page():

    links = re.findall('<a href="(.+?)"', res.text)

    for link in links:
        # 对一些无用的超链接进行排除
        if 'AJAX/index.php' in link:
            continue

        if link.startswith('/'):
            link = 'http://xxxxx' + link
        else:
            link = 'http://xxxxxxx' + link

        # 将爬取到的页面文件进行保存本地的操作
        resp = requests.get(link)
        filename = link.split('/')[-1] + time.strftime("_%Y%m%d_%H%M%S") + '.html'
        with open(f'./liutynotes/page/{filename}',mode='w') as file:
            file.write(resp.text)

def spider_image():
    res = requests.get('http://xxxxx/')
    images = re.findall('<img src="(.+?)"', res.text)
    for image in images:
        if image.startswith('/'):
            image = 'http://xxxxxx' + image
        else:
            image = 'http://xxxxxx' + image

        # 将爬取到的图片进行保存本地的操作
        resp = requests.get(image)
        filename = time.strftime("%Y%m%d_%H%M%S") + image.split('/')[-1]
        with open('./liutynotes/images/' + filename,mode='wb') as file:
            file.write(resp.content)

if __name__ == '__main__':
    spider_image()
