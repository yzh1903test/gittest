#！/usr/bin/python
#-*-c0ding:utf-8-*-
#OS内置模块，作用：python与PC系统进行交互
import  os
#1.获取当前目录的路径
os.getcwd()
print(os.getcwd())
#2.chdir(路径名)，作用：切换路径
os.chdir("OS_2")
print(os.getcwd())
#. 代表当前目录  ##os.curdir
print(os.curdir)
#.. 代表上一级目录  ##os.pardir
print(os.pardir)
os.chdir('..')
print(os.getcwd())
#"os.name"  获取操作系统的类型
print(os.name)
#创建多级目录   A/a/c   os.makedirs('a/c/dd')
#os.makedirs('A/c/555')
#创建单个目录
#os.mkdir('1903博文')
#删除多个必空目录
#os.removedirs('A/c/555')
#删除单个必空目录
#os.rmdir('1903博文')
#查看当前路径下所有的文件目录
d=os.listdir(r'D:\PycharmProjects\untitled')#('绝对路径名字')
print(d)
#对文件、目录进行重命名  os.rename('老名字','新名字')
#os.rename(r'D:\PycharmProjects\python 命令','D:\PycharmProjects\python类linuax命令')
#删除文件 os.remove(‘绝对路径’)
#os.remove(r'D:\PycharmProjects\python 类linuax命令\a.txt')
#执行OS内核命令 os.popen（'需要执行命令'）
c=os.popen('dir')
print(c.read())
#os.path 类 对文件的操作，返回文件的路径  例如返回文件的路径  判断文件、目录等
#1.返回文件的绝对路径 os.path.abspath（'文件名'）
a=os.path.abspath('kkk.jpg')
print(a)
#2.返回上一级目录'dirname(目录名)' /a/b/c/d/a.txt   ---->/a/b/c/
s=os.path.abspath(r'D:\PycharmProjects\untitled\lianxi.py')
print(s)
#3.返回当前文件/目录名 basename('路径')
e=os.path.abspath(r'D:\PycharmProjects\untitled')
print(e)
#4.判断文件/目录是否存在  ---->  "exists('路径名)"
print(os.path.exists(r'D:\PycharmProjects\untitled\lianxi.py'))
#5.判断是否为目录  isdir('路径名')
f=os.path.isdir(r'D:\PycharmProjects\untitled')
print(f)
#6.判读是否为文件  isfile('路径名')
x=os.path.isfile(r'D:\PycharmProjects\untitled\lianxi.py')
print(x)
#7.判断是否为连接文件  islink('路径名')
g=os.path.islink(r'D:\PycharmProjects\untitled\lianxi.py')
print(g)
#8.路径拼接  join('路径1','路径2')  a b --->/a/b
a='_'
b='13456'
print(a.join(b))
print(os.path.join('/a/','b'))
#9.分离路径 split('/路径名')  将最后一个文件或目录分离
print(os.path.split(r'D:\PycharmProjects\untitled\\'))
#10.分离文件后缀名  splittext('文件名')    返回一个元组
o=os.path.splitext('a.txt')
print(o)


#统计untitled项目文件下有多少个文件，目录
a1=[]
a2=[]
b=os.listdir(r'D:\Users\1903\untitled')
for i in b:
    if os.path.isdir(i):
        a1.append(i)
    else:
        a2.append(i)
print(f'当前目录有:{len(a1)}个目录,{len(a2)}个文件')
#面向对象判断当前目录下目录与文件个数
# class any(object):
#     def __init__(self,a1):
#         self.a1 = a1
#     def any_1(self):
#         a2 = 0
#         a3 = 0
#         for i in os.listdir(self.a1):
#             print(i)
#             if os.path.isdir(i):
#                 a2=a2+1
#             elif os.path.isfile(i):
#                 a3=a3+1
#         print(f"目录{a2}个，文件{a3}个")
# asd = any(r'D:\PycharmProjects\untitled')
# asd.any_1()



# import time  时间模块  time datatime
import time
#1.sleep(浮点数/整数)
print('睡眠之前')
time.sleep(1)
print('睡眠之后')
#2.clock() 计算机执行代码时cpu花费的时间
print(time.clock())
#3.系统当前时间 time.ctime time.asctime
print(time.ctime())
print(time.asctime())
#.获取本地时区
print(time.localtime())
#4.格式化输出时间  strftime（‘关于时间的字符串’）
print(time.strftime('%A %B %H: %M: %S'))
#5.格式化解析时间字符串 strptime('关于时间的字符串')
print(time.strptime('30 Nov 00','%d %b %y')) # %y年份 %d一个月中的第几天 %b表示月份
#6.计算机元年  距今的时间 秒 time()
print(time.time())
'''
%a
本地化的缩写星期中每日的名称。

%A
本地化的星期中每日的完整名称。

%b
本地化的月缩写名称。

%B
本地化的月完整名称。

%c
本地化的适当日期和时间表示。

%d
十进制数 [01,31] 表示的月中日。

%H
十进制数 [00,23] 表示的小时（24小时制）。

%I
十进制数 [01,12] 表示的小时（12小时制）。

%j
十进制数 [001,366] 表示的年中日。

%m
十进制数 [01,12] 表示的月。

%M
十进制数 [00,59] 表示的分钟。

%p
本地化的 AM 或 PM 。
(1)
%S
十进制数 [00,61] 表示的秒。
(2)
%U
十进制数 [00,53] 表示的一年中的周数（星期日作为一周的第一天）作为。在第一个星期日之前的新年中的所有日子都被认为是在第0周。
(3)
%w
十进制数 [0(星期日),6] 表示的周中日。

%W
十进制数 [00,53] 表示的一年中的周数（星期一作为一周的第一天）作为。在第一个星期一之前的新年中的所有日子被认为是在第0周。
(3)
%x
本地化的适当日期表示。

%X
本地化的适当时间表示。

%y
十进制数 [00,99] 表示的没有世纪的年份。

%Y
十进制数表示的带世纪的年份。

%z
时区偏移以格式 +HHMM 或 -HHMM 形式的 UTC/GMT 的正或负时差指示，其中H表示十进制小时数字，M表示小数分钟数字 [-23:59, +23:59] 。

%Z
时区名称（如果不存在时区，则不包含字符）。

%%
字面的 '%' 字符。'''
#from datetime import  datetime,date,timedelta  精确导入
import datetime #整体导入
#1.获取当前时间、日期
print(datetime.datetime.now())
#2.获取指定的时间日期 datetime(整形数字)
print(datetime.datetime(2019,7,30,12,1,1))
#3.将时间的字符串转为datetime里的日期
t=datetime.datetime.strptime('1937-7-7 12:00:00','%Y-%m-%d %H:%M:%S')
print(t)
#4.将日期转化为字符串 strftime()
print(datetime.datetime.now().strftime('%H:%M:%S'))
#5.日期的加减
#求当前时间
a=datetime.datetime.now()
print(a)
#加3个小时
b=a+datetime.timedelta(hours=3)
print(b)
#6.只获取当前日期 today()
print(datetime.date.today())
#7.对日期进行加减
#步骤一：获取当前日期
#步骤二：加减日为期 timedelta(days=xxx)
f=datetime.date.today()+datetime.timedelta(days=45)
print(f)