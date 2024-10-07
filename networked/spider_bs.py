from bs4 import BeautifulSoup
import requests

res = requests.get('http://xxxxx/')
# 初始化构造一个解析器
jiexi_html = BeautifulSoup(res.text, 'lxml')
# 查找页面元素(按照层次结构一层一层)
print(jiexi_html.head.title.string)
print(jiexi_html.div)

# 查找页面元素的通用方法：
# 1、find_all:根据标签，属性，xpath等进行查找
# 2、select:CSS选择器,div,#id,.class

# 查找页面所有超链接
links = jiexi_html.find_all('a')
for link in links:
    print(link['href'])
# 查找页面所有的图片
images = jiexi_html.find_all('img')
for image in images:
    print(image['src'])

# 根据id或class属性进行查找
keywork = jiexi_html.find(id='keyword')
print(keywork)
title = jiexi_html.find_all(class_='title')
for titles in title:
    print(titles.find('a').string)

# 根据xpath风格进行查找 //div[@class='title']
title = jiexi_html.find_all('div',{'class':'title'})
for titles in title:
    print(titles.string)

# CSS选择器
tit = jiexi_html.select('div.title')
for tits in tit:
    print(tits.string)

keywords = jiexi_html.select('#keyword')
print(keywords[0]('placeholder'))

lis = jiexi_html.select('ul li')
print(lis)
