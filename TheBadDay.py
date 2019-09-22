#/user/bin/python
#-*-c0ding:utf-8-*-
#print(`内容`）:代码先执行内容，再执行打印
print ('hello world')
#input('提示语'):输入的都是字符
a= 'abcdefg'
print(a.upper())
b="ABCDEFG"
print(b.lower())
c='yan'.title()+'zhao'.title()+'hui'.title()
print(c)
f='WoRlD'
print(f.swapcase())
e='fewgfefwafe'
d=e.replace('fe','你好',3)
print(d)
g='bigcbigc'
print(g.split('c'))
h='beijing'
print(h.startswith('bei'))
i='bowenzhishneng'
print(i.endswith('eng'))
print('1516171'.split('1'))
i='-'.join('151617'.split('1'))
print(i)
l='%s是2019年7月%d日'%('今天',1)
print(l)
k=' space '
print(k.rstrip())
m=('123','456','789','10,11,12','123','456','789','123')
n=m.index('123',4)
print(n)
x=[123,456,789,123,456,789,'abc','def','abc','def','ghk']
x.append('sb')
print(x)
y=['nihao','nihao','123','123','123' ]
y.insert(2,'wobuhao')
print(y)
s=[12,23,12,13,23,2,1,3,23]
s.pop(1)
print(s)
z=[12,56,12,12]
z.remove(12)
print(z)
z.remove(12)
print(z)
j=[5,8,6,0,7,9,3,10,4,1,3,2,10]
j.sort()
print(j)
o=[56,79,63,'坑逼']
j.extend(o)
print(j)
print('%s是你的第%d个爸爸'%('他',1))


s = input('请输入一个字符串：')
if not s:
    print('请不要输入空字符串！')
    s = input('请重新输入一个字符串：')
a = reversed(list(s))
if list(a) == list(s):
    print('您所输入的字符串是回文')
else:
    print('您所输入的字符串不是回文')



a=input('输入一个字符串')
b=a[::-1]
if a==b:
    print('你输入的字符串是回文')
else:
    print('你输入的字符串不是回文')
r=[4,1,7,5,78]
print(r.sort(reverse=True))