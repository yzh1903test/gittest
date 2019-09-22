#！/usr/bin/python
#-*-c0ding:utf-8-*-
import re
import requests
w={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
                                                                                                                                      }
r = requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/',headers=w)
data = r.content.decode(encoding='gbk')
# print(data)

a = re.compile(r'<dd><a href="(.*?)">(.*?)</a></dd>')
b = re.findall(a,data)
print(b)

ff = []
for i in b :
    b = requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/{}'.format(i[0]) )
    q = b.content.decode(encoding='gbk')
    r2 = re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />')
    f1 = re.findall(r2,q)
    for j in f1:
        u = open(r'D:\PycharmProjects\untitled\python小说爬虫数据.txt', 'a')
        u.writelines(j)
        u.close()
