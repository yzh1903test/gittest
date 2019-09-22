#！/usr/bin/python
#-*-c0ding:utf-8-*-
#Python3.7 冒泡排序法
# a=[19,65,24,36,17,985,211,360,119]
# b=len(a)
# for i in  range(b):
#     for j in range(b-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
#Python3.7 选择法排序
# c=[19,65,24,36,17,985,211,360,119]
# d=len(c)
# for x in range(d):
#     for y in range(x+1,d):
#         if c[x]>c[y]:
#             c[x],c[y]=c[y],c[x]
# print(c)
# #Python3.7 100以内质数之和
# e=0
# for f in range(1,101):
#     for g in range(2,101):
#         if f%g==0:
#             break
#     if f==g:
#         e=e+g
# print(e)
# #Python3.7 水仙花数
# l=[]
# for h in range(100,1000):
#     baiwei=h//100
#     shiwei=(h//10)%10
#     gewei=h%10
#     if h==(baiwei**3+shiwei**3+gewei**3):
#         l.append(h)
# print(l)
# #Python3.7 任意数字的阶乘之和
# n=1
# sum=0
# m=int(input('请随意输入一个正整数数字：'))
# if m<0:
#     print('负数没有阶乘')
# elif m==0:
#     print('0的阶乘为1')
# else:
#     for k in range(1,m+1):
#         n=n*k
#         sum=sum+n
#         print(n)
# print('%d的阶乘之和为:%d'%(m,sum))
#Python3.7  6位验证码(函数)
# import string,random
# yanzhengma=''
# words = ''.join((string.ascii_letters, string.digits))#"string.ascii_letters"随机生成大小写字母;"string.digits"随机生成0-9数字！
# for i in range(8):
#     yanzhengma += random.choice(words)#random.choice （），随机选取字符串、列表等
# print(yanzhengma)
# b=input('请输入验证码：')
# if b==yanzhengma:
#     print('验证码输入正确')
# else:
#     c=input('验证码输入不正确！请重新输入：')
#     print(c)
#     print('验证码输入正确')
# #Python3.7  列表左移一位
# a=[1,3,4,7]
# a.insert(4,1)
# print(a)
# a.pop(0)
# print(a)
#大于等于2任意整数质数数之和(函数)
def fun(a):
    d=0
    for i in range (2,a):
        for j in range(2,i+1):
            if i%j==0:
                break
        if i==j:
            d+=i
    print(d)
    return fun
fun(100)
#定义一个函数，函数有一个可变长参数：kwargs
#1.获取kwargs传入的所有键、值
#2.判断kwargs的每个值类型，统计有多少个字符串、列表、元组、集合、数值、字典类型的个数
#3.如果某个类型的值大于等于3，函数终止，并返回由这些类型的值组成的列表
def j (**kwargs):
    b=kwargs.keys()
    a=kwargs.values()
    # print(a)
    # print(b)
    c=[]
    d=[]
    e=[]
    f=[]
    g=[]
    h=[]
    for i in kwargs.values():
        if type(i)==tuple:
            c.append(i)
            if len(c)>3:
                break
        elif type(i)==list:
            d.append(i)
            if len(d)>3:
                break
        elif  type(i)==str:
            e.append(i)
            if len(e)>3:
                break
        elif type(i)==dict:
            f.append(i)
            if len(f)>3:
                break
        elif type(i)==int:
            g.append(i)
            if len(g)>3:
                break
        else:
            h.append(i)
            if len(h)>3:
                break
    print('字符串元素有',len(c), '个')
    print('元组元素有', len(d), '个')
    print('数值元素有', len(e), '个')
    print('字典元素有', len(f),'个')
    print('列表元素有', len(g), '个')
    print('集合元素有', len(h), '个')
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
j(a1 = 1,a2 = 2,a3 = [1,2,3],a4  = 'a',a5 = 'b',a6 = ['p'],a7 = {1,2},a8 = {'a':1},a9 = ['a'],a10 = ['n'],a11 = 7,a12=('a',))
#函数：形参(变量) 参数的数量理论无限，但实际中最好不超过6,、7个，参数类型不限
def func(name,age,hobby):
    print('%s is a good man! he is %d years old! he like %s、%s and %s'%(name,age,hobby[0],hobby[1],hobby[2]))
#函数在调用时，需要给函数按顺序传递数据，数量要对应
#实际参数:即值
func('yzh',24,['money','driver','computer'])
#定义一个类（面向对象)
class zool(object):  #（继承于哪个类）#object翻译成中文是对象#object所有类的基类

    animal='老虎'
#方法
    def biaoyan(self): #(self,在方法里必填的的一个参数;self指代对象本身！)
        print(f'有个神奇动物在表演，{self.animal}在表演')

#类的使用
zool()
a=zool()#创建对象
#使用对象的方法、类
print(a.animal)#a对象
a.biaoyan()
#类的组成
# 一、属性：
# 1.从公有私有角度
#    公有属性
#    私有属性
# 2.从类、对象角度
#     类属性
#
#     对象属性==实例属性
# 二、方法
#学生类
class Student(object):
    #类的属性
    name='大帅哥'
    Class='1903'
    sex=True#男生True
    book=['言情系列','武侠系列','都市系列','玄幻系列']
#初始化方法
    def __init__(self,name,Class,sex):
        #对象的属性
        self.name=name #例如name的值为张三
        self.Class=Class
        self.sex=sex
        #print(f'有个学生的名字叫做{self.name}')
#打印学生姓名
    def print_name(self):
        print(f'有个学生的名字叫做{self.name}')
#打印学生班级
    def print_Class(self):
        print(f'有个学生叫{self.name}，在{self.Class}班级里，他Python学的贼棒')
#打印学生性别
    def print_sex(self):
        if self.sex:
            print('哇！靓仔')
        else:
            print('哇，靓女')
#打印学生书包书
    def print_book(self):
        for i in self.book:
            print(f'他书包里的书有：{i}')
#类可不可以使用对象的属性
'''类不能使用对象的属性'''
'''类名--->代表类'''
'''类可以使用自己的属性'''
print(Student.name)
print(Student.book)
#对象可不可以使用自己的属性
'''对象可以使用自身的属性'''
'''对象可以使用类的属性'''
A=Student('张三',1903,True)
print(A.book)
#def__init__(self): 初始化方法
# #使用类的代码
#B.print_book()
#老师类
class Teacher(object):
    #类属性(公有、私有# )
    kecheng=['语文','数学','英语','生物'] #公有属性
    __gread='1903' #私有属性;  私有属性标志：双英文__下划线开头
    def __init__(self,a,b,c):
        self.a=a #公有的对象单属性
        self.__b=b #私有的对象属性
        self.__c='hello  world'
    def kl(self):
        print(f'方法访问类的公有属性：{self.kecheng}')
        print(f'方法阿访问私有属性：{self.__grade}')
    def g(self):
        print(f'方法访问类的公有属性：{self.a}')
        print(f'方法访问类的私有有属性：{self.b}')
    def __w(self):
        print('这是一个私有方法')
#在类的外部使用对象，方法名来访问方法;在类的内部，使用self.方法名来访问方法
    def h(self):
        self.__w()
# @方法在Python中称为语法糖
    @classmethod  # 装饰器：将一个实例方法变成一个类方法
    def yzh(cls):
     print('这是一个类方法')
    @staticmethod  # 装饰器，将一个实例方法转为一个静态太方法
    def sb():
     print('这是一个静态方法')
print(Teacher.kecheng)
#类的私有属性不能在类的外部访问
#print(Teacher.__grade)
# t1=Teacher() #对象可以访问类的内部公有属性
# t1.kl()
# #print(t1__grade) #私有属性在类的外部无法访问
# t2=Teacher('hello python')
# print(t2.__b) #私有的对象不能在类的外部访问
# t2.g()
# #私有属性的目的:属性被定义不希望被更改;对象可以访问对象的私有属性和公有属性（在类的内部）
# #更改属性的对象值
# Teacher.kecheng=(1,2,3)
# print(Teacher.kecheng)
# #更改对象属性对象的值
# t3=Teacher(1,2,3)
# print(t3.c)
# t3.c='hello world'
# print(t3.c)
#方法：静态、类方法、实例【普通方法】、魔法方法、私有方法
#私有方法：
#def __方法名(self,参数)
#@方法在Python中称为语法糖
#面向对象3个特点
#1.封装：对数据、代码逻辑的处理
#2.继承：单继承、多继承
#1.>单继承：B类继承A类，只继承一类
#2.>多继承：

#3.多态


#单继承
class A(object):  #定义一个A类
    #类属性
    name='abc'
    age=18
    def __init__(self,a):
        #对象属性
        self.a=a
#实例方法
    def b(self):
        print('这是a类的实例方法b')
class B(A):  #定义一个B类
     def c(self):#实例方法
         print(f'父类的类属性有name:{self.name},age:{self.age}')
         self.b()  #在B类直接使用A类的方法
#子类拥有父类的所有属性与方法
#创建一个B类的对象
b=B('hello')
#子类能否使用父类的属性、方法
print(b.name)
print(b.a)
b.b()
b.c()






#匿名函数 “lambda” 减少代码量，无法取代def常规函数；常用来简单计算;只能写一行，一行中间不能中断，不支持循环，判断语句！
def a(x):
    return (x+1)
a(2)
f=lambda  x:x+1  #匿名求和
print(f(2))
c=lambda z,y:(y-3)*z  #匿名求差
print(c(0,100))
#面向对象的多态  要求：
# 子类的方法名与父类的方法名一样；
# 如果要是用父类的方法要在子类中定义一个函数，在函数里写：super().父类的方法名；
# 子类对象在使用父类方法时：对象.子类定义方法名
# a=0
# def f():
#     #a=100
#     print(a)
#f()
class c(object):
      def foo(self):
        print('这是C类的一个实例方法')
class D(c):
      def foo(self):
         print('这是D类的实例方法')
#         super()是一个对象
      def k(self):
        super().foo()
d1=D()
#d1使用D类的实例方法
d1.foo()
#d2使用c类的实例方法
d2=D()
d2.k()


#九九乘法表
for i in range(1,10):
 for j in range(1,10):
    print('%s×%s=%s'%(i,j,i*j),end=' ')
 print()