#！/usr/bin/python
#-*-c0ding:utf-8-*-
#爬虫:通过Python代码自动获取网络中的数据资源（文件、视频、音乐等）
#反爬虫：防止网络资源被爬虫代码获取
#反爬机制:属于反爬虫的技术手段机制
#最常见的反爬虫机制:
# 1.封锁IP地址
# 2.封锁机器物理Mac地址
# 3.验证码
# 4.服务器传输给浏览器的数据通过异步加载
'''
re 正则模块
requests  python发送http/https、请求、接受响应数据的一个第三方库
'''
import re
import requests
w={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
                                                                                                                                      }
#    "User-Agent" 代表Python伪装浏览器
#get 请求获取资源
#NO1.发送请求
x=requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/17125664.html',headers=w)
#NO2.获取响应的数据  content 方法获取
date=x.content.decode(encoding='gbk')
print(date)
print(type(date))
#"<h2> 第一章 雪鹰领</h2>"
r1=re.compile(r'<h2>.*?</h2>')
b=re.findall(r1,date)
print(b)
r2=re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />')
f=re.findall(r2,date)
print(f)

o=open(file='python小说爬虫数据.txt',mode='w',encoding='utf-8')
for i in f:
    o.write(f'{i}\n')

s=requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/',headers=w)
date_1=s.content.decode(encoding='gbk')
print(date_1)
r3=re.compile(r'<dd><a herf="(.*?)">(.*?)</a></dd>')
res=re.findall(r3,date_1)
print(res)