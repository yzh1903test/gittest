# #！/usr/bin/python
# #-*-c0ding:utf-8-*-
# #1.>>>冒泡排序
# a=[2008,1937,2019,1995,2020]
# b=len(a)
# for i in range(b):
#     for j in range(b-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
# #2.>>>选择排序法
# c=[2008,1937,2019,1995,2020]
# d=len(c)
# for x in range(d):
#     for y in range(x+1,d):
#         if c[x]>c[y]:
#             c[x],c[y]=c[y],c[x]
# print(c)
# #3.九九乘法表
# for i in range(1,10):
#   for j in range(1,10):
#      print('%s*%s=%s'%(i,j,i*j),end=' ')
#   print()
# #4.100以内质数之和
# e=0
# for i in range(1,101):
#     for j in range(2,101):
#         if i%j==0:
#             break
#     if  i==j:
#         e=e+j
# print(e)
# #5.n个整数阶乘之和
# f=1
# sum=0
# jc=int(input('请输入您想求的和数字：'))
# if jc <0:
#     print('负数没有阶乘！')
# elif jc==0:
#     print('0的阶乘为1')
# else:
#     for i in range(1,jc+1):
#         f=f*i
#         sum=sum+f
#         print(f)
# print('%d的阶乘之和为：%d'%(jc,sum))
# #函数阶乘之和
# def jiechengsum(a):
#     sum=0
#     b=1
#     for i in range(1,a+1):
#         b=b*i
#         sum=sum+b
#         print(sum)
#         return (sum)
# jiechengsum(10)
#
# #6.水仙花数
# g=[]
# for i in range(100,1000):
#     baiwei=i//100
#     shiwei=(i//10)%10
#     gewei=i%10
#     if i==(baiwei**3+shiwei**3+gewei**3):
#         g.append(i)
# print(g)
# #7.统计untitled下有多少文件，多少目录？
# import os
# class any(object):
#     def __init__(self,a1):
#         self.a1 = a1
#     def count(self):
#         a2=0
#         a3=0
#         for i in os.listdir(self.a1):
#             print(i)
#             if os.path.isdir(i):
#                 a2+=1
#             elif os.path.isfile(i):
#                 a3+=1
#         print(f"目录{a2}个，文件{a3}个")
# c=any(r'D:\Users\1903\untitled')
# c.count()
# #8.网络爬虫爬取文字，写入txt文本
# # import re
# # import requests
# # g=requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/')
# # date=g.content.decode(encoding='gbk')
# # print(date)
# # p=re.compile(r'<dd><a href="(.*?)">(.*?)</a></dd>')
# # b=re.findall(p,date)
# # o=open(file='FUXI.txt',mode='w',encoding='utf-8')
# # for i in b:
# #     o.write(f'{i}\n')
# #1234可以组成多少个不同的数
# f=0
# for y in range(1,5):
#     for z in range(1,5):
#         for h in range(1,5):
#             if (y!=z) and (z!=h) and (h!=y):
#                 print('{}{}{}'.format(y,z,h),end=' ')
#
# print('')
# print('共{}种组合'.format(f))
# # 不使用int将一个数字字符转换为int
# a =input("请输入一个数字:")
# b = a[::-1]
# for i,j in enumerate(b):
#      for h in range(100):
#          if str(h) == j:
#           b = h * (100 ** i)
# print(b)
# print(type(b))
import  os
a=os.mkdir('AAA')
a1=open(file='FUXI.txt',mode='w', encoding='utf-8')
a1.write('hello world')
os.remove('FUXI.txt')
os.rmdir('AAAAAAAA')
