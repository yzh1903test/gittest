# #/usr/bin/python
# #-*-c0ding:utf-8-*-
# print (45678+0x12fd2)
# print (2019-1995)
# print(2019*1995)
# print(2019/1995)
# print("learn Python in BowenZhiSheng")
# print(100<99)
# print(0xff==255)
# print(100+200)
# print("hello","world")
# x='me'
# y=x
# x=123
# print(y)
# x1 = 1
# d = 3
# n = 100
# x100 = x1 + (n - 1) * d
# s = (x1 + x100) * n / 2
# print (s)
# a=[12,3,4,5]
# b=a.index(3)
# print(b)
# a=[123,456,789]
# a.clear()
# print(a)
# b=a.copy()
# print(a)
# a=[12,23,[23,34],4]
# b=a.copy()
# a[2].append(0)
# print(b)
# import copy
# c=[12,23,[23,24],4]
# d=copy.deepcopy(c)
# c[2].append(0)
# print(d)
# a=[12,23,['qeq',123],'wqer']
# b=a.copy()
# a[2].append(13)
# print(a)
# print(b)
# e=[16,18,19,26,[26,28,29],11,56,77]
# f=copy.deepcopy(e)
# e[4].append('helloworld')
# print(e)
# print(f)
# a=[12,23,45,66]
# b=a.index(66)
# print(b)
# g={1,2,3,4,5,8,9}
# g.add(90)
# print(g)
# g.pop()
# print(g)
# k={'name':'ross','age':'24','sex':'女'}
# k.popitem()
# print(k)
# print(k.items())
# k['date']='1995-10-11'
# print(k)
# l={'sex':'男'}
# k.update(l)
# print(k)
# m={1,2,3,4,5,6}
# print(len(m))
# i=sum((1,2,2,3,4,5))
# print(i)
# a,b=divmod(18,4)
# print(a,b)
# a=100
# b=20
# c=a+b
# print(c)
# c=a-b
# print(c)
# c=a*b
# print(c)
# c=a/b
# print(c)
# c=a//b
# print(c)
# c=a**b
# print(c)
# s1=100
# s2=3
# d1=s1%s2
# print(d1)
# for i in range(1,10):
#      for j in range(0,10): #“3位的水仙花数”
#         for k in range(0,10):
#            if i*100+j*10+k==i**3+j**3+k**3:
#                 print(i*100+j*10+k)
# x="TOM Mao"
# print(f'你好{x}')
# s="I,KNOW,I,Beautiful"
# n=s.split(',',2)
# print(n)
# print(s.isspace())
# s='hello'
# print(s[::-2])
#
#
# a=[18,69,76,23,62,14]
# for i in range(len(a)):
#     for j in range(i):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
#
# for i in range(0):
#  print(i)
#
#
# l='I am {name},i live in {address} china'.format(name='yzh',address='shanghai')
# print(type(l))
# x=10.0
# print(type(x))
# print(4//2)
# print(type(4//2))
# print(bool(0))
# y=[1,2,3,4,'a',3.14,[456]]
# print(y[4],y[1])
# z=[4467,94,96,7]
# print(y+z)
#
# #1到4组合不重复三位数字的次数
# i = 0
# for x in range(1,5):
#     for y in range(1,5):
#         for z in range(1,5):
#                 if (x!=y) and (y!=z) and (z!=x):
#                     print('{}{}{}'.format(x,y,z),end=' ')
#                     i +=1
# print('')
# print('共{}种组合'.format(i))
#
# s3={1,2,3,4,5,6,7,8}
# s4={1,2,3,4,5}
# print(s4.issuperset(s3))
# #导入随机数库
# import random
# a=random.randint(1,99)
# print(a)
# #列表推导式
# print([i for i in range(101)if i%2==0])
# c=[]
# for i in range(100):
#     if i%2==0:
#      c.append(i)
# print(c)
# #一张纸折叠多少次达到珠穆拉马峰高度
# a,b = 0.00008,0
# while a < 8848:
#      a = a * 2
#      print(a)
#      b += 1
#print(b)
#账号长度在6～8之间为合法的账号
#密码的长度在5～7之间为合法的密码
#账号和密码都符合上述要求，将账号密码以键值对的形式保存
# usnumber=['ads','dafdsa','jjajs','dfdsdas']
# password=['fdsfd','fdsfdsaffdsa','','jjja','213232']
# z={}
# a = eval(input("请输入一个数字："))
# print(a)
# print(type(a))
# d={'卡号':123456,'密码':'adwaws'}
# d.pop('卡号')
# print(d)
# fruitl={'lemon':5,'apple':10,'pear':20}
# fruitl.setdefault('lemon',20)
# print(fruitl)
# print(list(fruitl))
# print(tuple(fruitl))
# print(str(fruitl))
# print(set(fruitl))
#100以内质数之和
# a=0
# for i in range(1,101):
#     for j in range(2,101):
#         if i%j==0:
#             break
#     if i==j:
#      a=a+i
# print(a)
# #三位水仙花数
# a=[]
# for i in range(100,1000):
#     gewei=i%10
#     shiwei=i//10%10
#     baiwei=i//100
#     if i==(gewei**3+shiwei**3+baiwei**3):
#         a.append(i)
# print(a)
# #任意正整数阶乘之和
# a=1
# sum=0
# j=int(input('请输入任意正整数：'))
# if j<0:
#     print('负数没有阶乘')
# elif j==0:
#     print('0的阶乘为：1')
# else:
#     for i in range(1,j+1):
#         a=a*i
#         sum=sum+a
# print('%s的阶乘之和为：%s'%(j,sum))

#函数阶乘之和
# def jc(a):
#      sum = 0
#      b = 1
#      for i in range(1,a + 1):
#          b=b*i
#          sum=sum+b
#      print(sum)
#      return sum
#jc(10)
# #函数质数之和
# def zs(a):
#      sum=0
#      for i in range(2,a):
#          for j in range(2,i+1):
#              if i%j==0:
#                  break
#          if i==j:
#             sum=sum+i
#      print(sum)
#      return sum
# zs(50)
