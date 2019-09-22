#！/usr/bin/python
#-*-c0ding:utf-8-*-
#1.九九乘法表
for a in range(1,10):
     for b in range(1,a+1):
         print('%s*%s=%s'%(a,b,a*b),end=' ')
     print()
#2.不使用int将一个字符转换为int
a=input("请输入一个字符:")
b= a[::-1]
for i,j in enumerate(b):
    for h in range(100):
      if str(h) == j:
       b=h*(100**i)
print(type(b))
print(a)
#3.创建文件删除文件
import  os
a=os.mkdir('CCC')
a1=open(file='测试.txt',mode='w', encoding='utf-8')
a1.write('hello world')
#os.remove('测试.txt')
#4.统计a.txt文件中有多少行，统计时去掉单行注释的行和空行
import re
with open(file='a.txt',mode='r',encoding='utf-8') as f:
    b=f.read()
    c=b.split('\n')
    d=len(c)
    r1=re.compile(r'#(.*?)')
    g=re.findall(r1, b)
    j=len(g)
    r2=re.compile(r'$')
    h=re.findall(r2, b)
    k=len(h)
print(f"共有{d}行，空行有{k}行，单行注释有{j}行，去除空行和单行共有{d-j-k}行")

#5.面向对象爬取糗事百科，并写入x.txt
import re
import requests
class A(object):
    def g(self):
        url="https://www.qiushibaike.com/text/"
        head={"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"}
        d=requests.get(url=url,headers=head)
        t=d.content.decode("utf-8")
        c=re.compile('<div class="content">(.*?)</span>',re.S)
        e=c.findall(t)
        for i in range(len(e)):
            with open("x.txt","a",encoding="utf-8")as f:
                f.write(e[i])
a=A()
a.g()
