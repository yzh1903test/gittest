#！/usr/bin/python
#-*-c0ding:utf-8-*-
import re
import requests
class photo(object):
    #类属性
    l= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
    def __init__(self):
        #局部变量
        x=requests.get(url='https://www.58pic.com/newpic/35180567.html',headers=self.l)
        #对象属性
        self.d=x.content.decode(encoding='gbk')#获取响应数据

    def fenxi(self):
        #打印源码文件
        #print(self.d)
        r1=re.compile(r'<img src="(.*?)" class="show-area-pic"')
        date=re.findall(r1,self.d)
        urls=[]
        for i in date:
            urls.append('https:'+i)
            return urls
        #print(date)
    def download(self):
         n=0
         for i in self.fenxi(): #包含4个图片的urls
           req=requests.get(url=i, headers=self.l)
           #接收响应结果
           jieguo=req.content
           #保存图片
           f=open(file=f'{n}.jpg',mode='wb')
           f.write(jieguo)
           n+=1
p1=photo()
p1.fenxi()
p1.download()

#库 包 模块
'''模块:一个.Py文件
   Python包：多个.Py文件构成 特点，必须存在一个__init__.py
   Python库:多个包，模块组成的一个集合
'''
#Python with语句
'''with上下文管理器
   "gc" 垃圾回收机制 --->释放不被释放的内存
'''
with open(file='a.txt',mode='w')as a:
    a.write('446794967')
