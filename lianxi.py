# #！/usr/bin/python
# #-*-c0ding:utf-8-*-
# #01.>"find()"   从左往右 查找字符串内元素，找到返回：1，未找到返回-1！
# #   >"rfind()"  从右往左 查找字符串内元素，找到返回：1，未找到返回-1！
# a='hellowoeld'
# print(a.find('el'))
# #1.>"lower"大写转小写
# a='WANG BAO BAO'
# b=a.lower()
# print(b)
# #2.>"title"首字母大写
# a='singsongs'
# b=a.title()
# print(b)
# #3.>"swapcase"大小写互换
# a='HeLlo worLD'
# b=a.swapcase()
# print(b)
# #4.>"replace"('内容',"替换内容",替换数量) 字符串中字符数据的替换
# a='QQ:446794967'
# b=a.replace('4','6',2)
# print(b)
# #5.>"split"('分割字段') 将字符数据分割为列表"[]"
# a='cuiyongyuan'
# b=a.split('y')
# print(b)
# #6.>"upper"小写转大写
# a='i love china'
# b=a.upper()
# print(b)
# #7.>"startswitch('开头内容') 判断字符串是否以括号内元素开头
# a='begining'
# b=a.startswith('be')
# print(b)
# #8.>"endswitch"('结尾内容') 判断字符串是否以括号内元素结尾
# a='lover is over'
# b=a.endswith('Over')
# print(b)
# #9.>以某个数据元素分割，将列表连接成新的字符串 '分隔符'.join(元素序列)
# a='lianajie'
# b=a.split('a')
# c='-'.join(b)
# print(b)
# print(c)
# #10.>占位格式化字符串 “{}”占位 a.format(b)
# a='{} love {}'
# b='i'
# c=a.format(b,'you')
# print(c)
# #11.>"%"占位 "%s"(可以填充所有字符);"%d"(只能填充数字)
# a='%s最爱的girs是我在%d年认识的:%s'%('我',2015,'王宝宝')
# print(a)
# #12.>"strip()"去掉字符串空格，"lstrip()"去除字符串左空格；"rstrip"去除字符串右空格
# a=' Bowenzhisheng '
# print(a.strip())
# #13.>"count(元素)" 统计元组中某元素的个数
# a=(44,67,94,96,7,67,94,67,96,44,67)
# print(a.count(96))
# # 14.>"index(元素)"  从左往右 查看元组中元素下标位置
# #    >"rindex(元素)" 从右往左 查看元组中元素下标位置
# a=(12,12,13,34,55)
# print(a.index(55))
# #15.>"append（填充的数据）" 向列表中添加数据（默认最后一行，一次只能添加一个数据）
# a=[2017,2018,2019]
# a.append(2020)
# print(a)
# #16.>"insert(x,数据)" 向列表指定下标位置添加数据
# a=['1903届',2019,'0711',2019,'0910']
# a.insert(3,'博文智生')
# print(a)
# #17.>"remove(要删除是数据)" 删除元组中的数据
# a=[201314,520,'那是不可能的']
# a.remove('那是不可能的')
# print(a)
# #18.>"pop(下标码)" 依据下标码删除列表中数据
# a=[1995,1997,2018,2019,2015]
# a.pop(4)
# print(a)
# #19.>"sort()" 排序 列表数数据的排序
# a=[44,6,12,1,-3,-18,99]
# a.sort()
# print(a)
# #20.>"reverse()"  列表数据的反转
# a=[44,6,12,1,-3,-18,99]
# a.sort()
# a.reverse()
# print(a)
# #21.>"extend(n)" 列表中数据的更新
# a=[12,34,56,78]
# b=[90,13,'我嘞个乖乖']
# a.extend(b)
# print(a)
# #22.>"clear()" 清空数据
# a=[446794,17629759,182119]
# a.clear()
# print(a)
# #23.>"copy()" 复制数据
# a=['I am your father','741','haha','哈哈哈']
# b=a.copy()
# print(b)
# #24.>"copy()" 浅复制：只复制外边一层，不复制内层数据
# a=[12,23,['qeq',123],'wqer']
# b=a.copy()
# a[2].append('sb')
# print(a)
# print(b)
# #25.>"copy()" 深复制：全部层复制
# import copy
# a=[12,23,['qeq',123],'wqer']
# b=copy.deepcopy(a)
# a[2].append('sb')
# print(a)
# print(b)
# #26.>"add(要添加的数据)" 集合内添加数据且只能添加一个
# a={1213,1679,1903,1812}
# a.add(2019)
# print(a)
# #27.>字典获取所有的主.键  字典：{'key':'values'} 键值对格式
# a={'name':'cuixiaoyi','age':'24'}
# print(a.keys())
# #28.>字典获取所有的值
# a={'name':'cuixiaoyi','age':'24'}
# print(a.values())
# #29.>字典获取所有的键值对
# a={'name':'cuixiaoyi','age':'24'}
# print(a.items())
# #30.>"a['key']='value'" 字典添加数据（没有数据就添加，有数据就更改）
# a={'name':'cuixiaoyi','age':'24'}
# a['sex']='men'
# #31.>"pop('键名')" 删除字典内数据
# a={'name':'wangbaobao','age':'22'}
# a.pop('name')
# print(a)
# #32.>"popitem()" 默认删除字典最后一个键值对数据
# a={'name':'cuixiaoyi','age':'24','sex':'女'}
# a.popitem()
# print(a)
# #33.>"update(n)" 字典内数据更新
# a={'name':'cuixiaoyi','age':'24','sex':'女'}
# b={'性格':'NAIKAO'}
# a.update(b)
# print(a)
# #34.>"set()" 去重 去掉对象(元组，列表，集合，字典)内重复数据
# a={12,12,13,13,14,14,15,15}
# b=set(a)
# print(a)
# #35.>"type(变量与数据)"  查看数据类型
# print(type('你是什么垃圾？'))
# print(type(True))
# print(type(446794967))
# #36.>"len(变量和数据)"  统计元素有多少个
# a='lear Python in Bo wen Zhi Sheng'
# print(len(a))
# #37.>"enumerate()" 显示列表元素对应下标及下标对应内容
# a=['HUAWEI','HONOR','Apple','xiaomi','oppo','vivo','other']
# for i,j in enumerate(a):
#     print(i,j)
# #38.>"进制的转换"
# print(hex(192))  #十进制数转换为十六进制数：hex(192)
# print(oct(192))  #十进制数转换为八进制数：  oct(176)
# print(bin(192))  #十进制数转换为二进制数：  bin(192)
# print(int(0x060))#任何进制数转换为十进制数:int(192)
# print(chr(98))   #将数字转换为ASCII表对应的字符：char(98)
# print(ord('y'))  #将ASCII表中字符转换为数字：ord('n')
# #39.>"sum((1,2,3,4))" 求和
# print(sum((2015,2016,2017,2018,2019)))
# #40.>"整数求余" a,b=divmod(a,b) a是整除的结果，b是求余的结果
# a,b=divmod(16,17)
# print(a,b)
# #.>"max","min"  返回最大最小值
# #41.>if 条件语句
# # if False:
# #     print('I love Python!')
# # else:
# #     print('I hate Python!')
# # #42.>"天猫登录脚本"
# # a=int(input('输入登录账号:'))
# # b=int(input('输入登录密码:'))
# # if   a==44679496 and b==19951022:
# #     print('登录成功')
# # else:
# #     print('登陆失败')
# # #43.>"判读学生成绩"  要求随意输入一个成绩，判断学生成绩的情况
# # c=int(input('输入成绩：'))
# # if c>100:
# #         print('输入成绩无效')
# # elif  90<=c<=100:
# #         print('成绩优秀')
# # elif  80<=c<90:
# #         print('成绩良好')
# # elif c>=60 and c<80:
# #         print('成绩一般')
# # else:
# #         print('成绩不及格')
# #44.>elif多条件判断
# # cunkuan=int(input('请输入存款金额： '))
# # if cunkuan>=100:
# #     print('买宝马')
# # elif cunkuan>=50:
# #     print('买丰田')
# # elif cunkuan>=20:
# #     print('买国产车')
# # else:
# #     print('办月卡骑共享单车！')
# #46.>python成员运算符 "in" 在...里面；"not in" 不在...里面
# a=[1,2,3,4,5]
# print(6 not in a)
# #47.>逻辑运算符 "and" 与 两个条件同时满足；"or" 或 满足一个条件即为真;"not" 非 真则价，假则真！
# #数值：0，空字符串‘adad’，空列表[]，空集合{}，空元组()，空字典；默认输出：False
# #None空的 --->函数的返回值的一种
# #48.for循环  for i in xx： 代码语句  "xx"--->代表可迭代的对象
# #for循环一个字典的时候，print：“键！”  for循环可：字符串，列表，元组，集合，字典！
# str_1={'name':'jack','age':'45'}
# for i in str_1:
#     print(i)
# #49.>去掉列表中重复的数据  要求：不得调用列表去重函数“set”，不得用字典键值对！
# a=[1,2,3,4,5,1,2,3,6,6,7]
# b=[]
# for i in a:
#       if i not in b:
#           b.append(i)
# print(b)
# #50.>九九乘法表
#

# a=[[1,],'zifu',68,(1,6),{5,9},{'a':'弟弟'}]
# print(a)
# #字典：
# #51."fromkeys(seq,value):"新建字典，设置默认值
# #seq：传入一个有序的对象，列表，元组，字符串
# #value:设置字典键对应的值，可以不写 None代表空
# s='abc'
# v=[1,2,3]
# d=dict.fromkeys(s,v)
# print(d)
#51.>"eval()" 将字符串当成有效的表达式来求值并返计算结果
#原型：ecal(*args,**kwargs)
#
# d = {
#     "data": {
#         "msg":
#         [
#             {
#                 "s_1": ["Jim", "男",  19, "175cm"],
#                 "country": "美国"
#             },
#             {
#                 "s_2": ["Kity", "女",  17, "165cm"],
#                 "country": "法国"
#             },
#             {
#                 "s_3": ["Tom", "男",  19, "173cm"],
#                 "country": "美国"
#             },
#             {
#                 "s_4": ["拖拉斯基", "男",  18, "180cm"],
#                 "country": "俄罗斯"
#             },
#             {
#                 "s_5": ["阿卡丽", "女",  17, "175cm"],
#                 "country": "乌克兰"
#             },
#             {
#                 "s_6": ["牙买稻子", "女",  18, "161cm"],
#                 "country": "日本"
#             },
#             {
#                 "s_7": ["龟田一郎", "男",  19, "175cm"],
#                 "country": "日本"
#             },
#             {
#                 "s_8": ["张三", "男",  20, "180cm"],
#                 "country": "中国"
#             },
#             {
#                 "s_9": ["李秀琴", "女",  19, "175cm"],
#                 "country": "中国"
#             },
#             {
#                 "s_10": ["宋仲基", "女",  19, "175cm"],
#                 "country": "韩国"
#             },
#             {
#                 "s_11": ["金正鞋", "男",  19, "168cm"],
#                 "country": "朝鲜"
#             },
#             {
#                 "s_12": ["卡列夫斯基", "男",  21, "190cm"],
#                 "country": "俄罗斯"
#             },
#         ]
#     },
# }
# #print(d)
# d1=d['data']['msg']
# name=[]
# sex=[]
# age=[]
# height=[]
# country=[]
# for i in d1:
#     for j in i.values():
#         if type(j)==list:
#             name.append(j[0])
#             sex.append(j[1])
#             age.append(j[2])
#             height.append(j[3])
#         else:
#             country.append(j)
#             e=set(country)
# print(name)
# print(sex)
# print(age)
# print(height)
# print(country)
#
#
#
#
#
#
#
# # 求国家个数
# print(d.values())
# print(d.keys())
# a=d['data']
# b=a['msg']
# c=set()
# for i in b:
#     e=i['country']
#     c.add(e)
# print(len(c))
# # 求所有学生的身高范围
# e = []
# for i in d["data"]["msg"]:
#   for i in d["data"]["msg"]:
#     a,c=i.keys()
#     for b in range(1,13):
#        if "s_" + str(b) == a:
#         e.append(i["s_" + str(b)][-1])
#         e.sort()
# print(f"身高范围{e[0]}-{e[-1]}")
# # 求统计男女比例
# e = []
# for i in d["data"]["msg"]:
#      a,c=i.keys()
#      for b in range(1,13):
#         if "s_" + str(b) == a:
#             e.append(i["s_" + str(b)][1])
# print(e)
# m = e.count("男") / e.count("女")
# print(f"男女比列{m}")
#
# # 求平均身高
# e = []
# for i in d["data"]["msg"]:
#     a,c=i.keys()
#     for b in range(1,13):
#         if "s_" + str(b) == a:
#             e.append(i["s_" + str(b)][-1])
# print(e)
# g = []
# h = 0
# for m in e:
#    h = int(m.rstrip("cm")) + h
# g = h / len(e)
# print(f"平均身高{g}cm")
#
# # 查询身高在170到180之间的学生名字
# e = []
# for i in d["data"]["msg"]:
#     a,c=i.keys()
#     for b in range(1,13):
#         if "s_" + str(b) == a:
#             # e.append(i["s_" + str(b)][-1])
#             if  170 <= int(i["s_" + str(b)][-1].rstrip("cm")) <=180:
#                 print(i["s_" + str(b)][0],i["s_" + str(b)][-1])
#
#
# #52.
# text = "Early in the day it was whispered that we should sail in a boat, " \
#         "only thou and I, and never a soul in the world would know of this our pilgrimage to no country and to no end"
# # # 1、将text中每个首字符大写的英文单词添加到一个列表中
# # a=(text.split())
# # b=[]
# # for i in a:
# #    if i.istitle():
# #        b.append(i)
# # print(b)
# # #2、将首字符小写的单词转换为首字符大写
# # 方法一：print (text.title())
# # list(text)
# # a=[]
# # for i in text:
# #         if i==i.title():
# #             a.append(i)
# # print(a)
# # # 3、将text中所有的包含a的字符替换成博文两个字
# # print(text.replace('a','博文'))
# # 4、删除包含小t字符的单词后，组成一个新的字符串
# l=text.split()
# for i in l:
#     if 't'in i:
#         l.remove(i)
# print(''.join(l))
# #冒泡法排序
# a = [0,94,44,67,96,7,19,3,789,4,13]
# b= len(a)
# for i in range(b):      #循环的最大次数
#    for j in range(b-1): #循环比较换位的最大次数减1
#       if a[j]>a[j+1]:
#          a[j],a[j+1]=a[j+1],a[j]
# print(a)
#
# #选择排序法
# lt = [3, 5, 2, 1, 8, 6,7,4,998,211,56,74,110,16]
# #求出lt的长度
# n = len(lt)
# #外层循环确定比较的轮数，x是下标，lt[x]在外层循环中代表lt中所有元素
# for x in range(n):
#    #内层循环开始比较
#    for y in range(x+1,n):
#       #lt[x]在for y 循环中是代表特定的元素，lt [y]代表任意一个lt任意一个元素。
#       if lt[x]<lt[y]:
#          #让lt[x]和lt列表中每一个元素比较，找出小的
#          lt[x],lt[y]=lt[y],lt[x]
# print(lt)
# 不使用int将一个数字字符转换为int
# a =input("请输入一个数字:")
# b = a[::-1]
# for i,j in enumerate(b):
#      for h in range(100):
#          if str(h) == j:
#           b = h * (100 ** i)
# print(b)
#print(type(b))
# #商品购物车
# # s=['香蕉','菠萝','提子','萝卜']
# # p=[100,80,50,30]
# # k=[20,30,15,45]
# # print(f"商品编号\t\t\t商品名\t\t\t商品价格\t\t\t库存量")
# # for i,j in enumerate(s):
# #     print('{}    \t\t\t{} \t\t\t{}  \t\t\t'.format(i,j,p[i]),k[i])
# # c=int(input('请输入要购买的商品编号:'))
# # if 0<=len(a):
# #           d=int(input('请输入购买数量:'))
# #           if 0<(d):
# #               v=input('是否使用会员卡？yes or no！:')
# #               if e=='yes':
# #                   vn=input('请输入会员卡号：')
# #                   if vn in['**********']:
# #                       print('对应金额为{}元'.format(b[int(c)]*int(d)*0.95))
# #                   else:
# #                       print('会员卡号错误！')
# #               elif v=='no':
# #                   print('应付金额为{}元'.format(b[int(c)]*int(d)))
# #               else:
# #                print('输入账号无效请重新输入“yes”或“no”')
# #       else:
# #           print('商品库存不足！')
# # else:
# #   print('编号输入错误！')
#
# #账号长度在6～8之间为合法的账号
# #密码的长度在5～7之间为合法的密码
# #账号和密码都符合上述要求，将账号密码以键值对的形式保存
# a=['ads','dafdsa','jjajs','dfdsdas']
# b=['fdsfd','fdsfdsaffdsa','','jjja','213232']
# c=len(a)
# d=[]
# e=[]
# for i in range(c):
#     if len(a[i])>=6 and len(a[i])<=8 and len(b[i])>=5 and len(b[i])<=6:
#         print(a[i])
#         print(b[i])
#         d.append(a[i])
#         e.append(b[i])
# if len(e)>=1:
#     # d1=''.join(d)
#     # e1=''.join(e)
# # d2=int(d1)
# # e2=int(e1)
#     print(len(e))
#     f = {}
#     f['账号']=d
#     f['密码']=e
#     print(f)
# else:
#     print('没有符合')
#
#
# n = int(input())
# jie = 1
# sum = 0
# i = 1
# while n >= i:
#   jie = jie * i
#   sum = sum + jie
#   i = i + 1
# print(sum)
#
#
# #无参数无返回值自定义函数
# def add():
#     a=0
#     for i in range(101):
#         a+=1
#     print(a)
# add()
# #函数的使用
# #1.先写函数名
# #2.()如果有参数则传参
#有参数无返回值！         "x" 必填参数
# def add(x):
#     a=0
#     for i in range(x):
#         a+=i
#     print(a)
# add(x=100)
#全局变量：定义一个变量后，在整个脚本的任意地方可使用
#局部变量：定义一个变量后，只能在特定范围之内使用
#有参数有返回值    ***当一个函数无返回值时，print返回结果为：None！***
# def add(x):
#     a=0
#     for i in range(x):
#         a+=i
#     print(a)
#     return a #1.返回值 2.表识一个函数的结束
# #    print('傻屌')#当return返回值时，函数代码已结束
# print(add)#函数在内存中的位置
# add(3)
# print(add(3))
# a=1000#全局变量（534行随意用）
# def cha(x1,x2):
#     #局部变量
#     b=10000
#     chazhi=b-x1-x2
#     print(b)
#     return chazhi
# print(cha(100,10))

#默认参数  函数使用时不对默认参数赋值，就使用默认值！若赋值，就是用传入值
# def f(x,y=100):  #y=100为默认值
#     print(x+y)
# f(100)

#匿名函数 “lambda” 减少代码量，无法取代def常规函数；常用来简单计算;只能写一行，一行中间不能中断，不支持循环，判断语句！
def a(x):
    return (x+1)
a(2)
f=lambda  x:x+1  #匿名求和
print(f(2))
c=lambda z,y:(y-3)*z  #匿名求差
print(c(0,100))

#*args可变长参数 1.可传入对个值 2.传入的值输出为一个元组
# def d(*args):
#     a,b,c=args
#     print(a)
#     print(b)
#     print(c)
#     print(args)
# d(123)
#**kwargs可变长传参 1.传入值以字典形式 a1=2,a2=3,a3=4
# def a(**kwargs):
#     x,y,z=kwargs #字典可使用字典所有方法
#     print(x)
#     print(y)
#     print(z)
# a(c1=2,c2=3)
#定义一个可以输入可变长参数的函数 *args
# 如果输入的参数的个数为0，提示输入“请为参数赋值，输入2个或4个数字，以英文逗号隔开”
#如果输入的参数是2个，求这两个数范围内的阶乘之和，例如输入的是1,5，求的就是1到5的阶乘
#如果输入的参数是4个，求这四个数能组成所少个不相同的四位数
#其他情况一律提示“该函数不执行！”
#print(tongji(1,5,6,7,8,9))
#定义一个函数，函数有一个可变长参数：kwargs
#1.获取kwargs传入的所有键、值
#2.判断kwargs的每个值类型，统计有多少个字符串、列表、元组、集合、数值、字典类型的个数
#如果某个类型的值大于等于3，函数终止，并返回由这些类型的值组成的列表
def j (**kwargs):
    a=kwargs.keys()
    b=kwargs.values()
    #print(a)
    #print(b)
    tuple_1=[]
    list_1=[]
    str_1=[]
    set_1=[]
    dict_1=[]
    int_1=[]
    float_1=[]
    bool_1=[]
    for i in kwargs.values():
        if type(i)==tuple:
            tuple_1.append(i)
            if len(tuple_1)>3:
                break
        elif type(i)==list:
             list_1.append(i)
             if len(list_1)>3:
                 break
        elif type(i)==str:
             str_1.append(i)
             if len(str_1)>3:
                 break
        elif type(i)==set_1:
             set_1.append(i)
             if len(set_1)>3:
                 break
        elif type==dict:
             dict_1.append(i)
             if len(dict_1)>3:
                 break
        elif type(i)==int_1:
             int_1.append(i)
             if len(int_1)>3:
                 break
        elif type(i)==float_1:
             float_1.append(i)
             if len(float_1)>3:
                 break
        elif type(i)==bool_1:
             bool_1.append(i)
             if len(bool_1)>3:
                 break
    print('元组元素有:',len(tuple_1),'个')
    print('列表元素有:', len(list_1), '个')
    print('字符串元素有:', len(str_1), '个')
    print('集合元素有:', len(set_1), '个')
    print('字典元素有:', len(dict_1), '个')
    print('整数型元素有:', len(int_1), '个')
    print('浮点型元素有:', len(float_1), '个')
    print('布尔值元素有:',len(bool_1),'个')
    print(tuple_1)
    print(list_1)
    print(str_1)
    print(set_1)
    print(dict_1)
    print(int_1)
    print(float_1)
    print(bool_1)
j(a1 = 1,a2 = 2,a3 = [1,2,3],a4  = 'a',a5 = 'b',a6 = ['p'],a7 = {1,2},a8 = {'a':1},a9 = ['a'],a10 = ['n'],a11 = 7,a12=('a',))
#定义一个函数，函数有一个必填参数x，一个默认参数y=[1,2,3,4,5,6,7,8,9]
#NO1：如果必填参数的值在默认参数内，则将y中对该数字的索引值之前的所有元素一次放到列表的后面
#例如：传入的值是2那么新的列表为y--->[3,4,5,6,7,8,9,1,2]
#NO2:若不存在y列表内，随机删除2个元素，再将x的值插入到列表索引值为5的位置
import random
k = []
v = []
def func(x, y=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print(f'x的值为：{x} , y的值为：{y}')
    if x in y:
        for j in range(x, len(y)):
            v.append(y[j])
        for q in range(0, x + 1):
            v.append(q)
        return f'x的值为：{x} , y的值为：{v}'
    else:
        for i in range(2):
            a = random.choice(y)
            k.append(a)
        print(f'随机数为：{k}')
        y.remove(k[0]),y.remove(k[1]),y.insert(5, x)
        return f'x的值为：{x} , y的值为：{y}'
# print(func(2))
# print(func(0))
b = input("请输入:")
if b.isdigit():
    print(func(int(b)))
#定义函数一：参数x为必填参数，参数y为可变长参数
#求函数一传入x的值+传入y的值的和
#定义函数二：必填参数z，z传入的是一个列表 例如：z--->['a','b',1]
#要求：以z作为字典的建，函数一的返回值作为字典的值，组成一个新字典
# zi={}
# def zidian_1(x,*args):
#    sum_1=sum(args)
#    u=x+sum_1
#    return u
# def zidain_2(z):
#     return z
# i=zidian_1(1,1,2)
# y=zidain_2([1,2,3])
# e=zi.fromkeys(y,i)
# print(e)
# #设计一个用户登录后生成session的函数，x为用户名，y密码
# #当用户密码都输入正确时，将用户名和密码组成一个新的字符串，随机取6~8位字符作为用户登录后的session
# #当用户名和密码组成的字符串'A'长度小于8位数时，自动添加0~9任意数字到'A'，再随机生成6~8位字符作为登录后的session
# import random
# d = {'admin':'12345','abc':'123','user':'54321'}
# def session(x,y):
#     A = ''
#     for i,c in d.items():
#         if x == i and d[i] == y:
#             A = x + y
#             while True:
#                 if len(A) >= 8:
#                     a = random.randint(6,8)
#                     b = ''
#                     for j in range(a):
#                         q = random.choice(A)
#                         b += q
#                     return f'这是session：{b}'
#                 else:
#                     e = random.randint(0,9)
#                     f = str(e)
#                     A += f
#     else:
#         return '请重新输入用户名和密码'
# print(session('admin','12345'))
# print(session('abc','123'))
# print(session('admin',2))
#嵌套函数
#def k()
#     print('k 函数的代码')
#     n=0
#     for i in range(10):
#         n+=i
# def f():
 #     k()
# f()
#Python对文件的操作
# f=open(file='a.txt',encoding='utf-8')#打开文件
# #读取文件
# print((f.read()))#读取文件全部内容
# print((f.readlines()))#以列表形式读取文件内容
#f=open(file='a.txt',mode='w',encoding='utf-8')
#f.write('hello pythoon')
#f=open(file='a.txt',mode='a',encoding='utf-8')
#f.write('\nhello world')
f=open(file=r'C:\Users\yzh2019\Desktop\sss.jpg',mode='rb')#打开照片
#将照片里的内容以二进制的形式读取出来
x=open(file='kkk.jpg',mode='wb')#打开另一张照片
x.write(f.read())#向照片添加二进制数据
#"file"文件名或文件在计算机的存放路径（必填参数）
#"mode" r表示读取；w表示写入（若文件不存在则自动创建）；x表示创建一个文件并写入数据到文件；a表示向文件里最后一行添加数据；b表示二进制显示文件，rb应用于读取资源到网络，wb表示读取资源到网络
#写两个函数，函数一:读取电脑中任意位置的txt文件，读取文件里的所有内容
# 函数二：向txt文件中可以追加写入数据，保存文件位置由user自选



