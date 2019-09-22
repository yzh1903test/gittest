#！/usr/bin/python
#-*-c0ding:utf-8-*-
#1.导入pymysql模块
import pymysql #连接数据库的专用库4588888
#2.与mysql建立连接
d=pymysql.connect(
    host='127.0.0.1', # 数据库所在的主机IP地址/域名【云服务器--mysql数据库】
    port=3306,  # mysql的端口号
    user="root", # mysql的用户名
    password="446794",  # mysql的用户密码，授权密码
    charset="utf8", # mysql数据的编码方式
    # database="1903博文测试",  # 指定数据库，不写这个参数，默认使用所有的数据库
)
#3.创建一个游标;mysql进入命令行模式
e=d.cursor()
#4.写SQL语句
sql='show databases'
#5.执行Sql语句  "execute"放入传入的sql语句，执行sql语句
data=e.execute(sql)#执行一条sql语句
#data_1=e.executemany(sql)#执行多条sql语句
print(data)
#print(data_1)
'''查询具体结果
print(e.fetchall())#查询执行sql后的所有结果
e.fetchone()#查询执行sql后的第一个结果 若无结果返回 None或-1
e.fetchmany(数字)#查询执行sql后的指定条结果
                                  '''
print(e.fetchmany(1))
print(e.fetchone())

#创建一个库
# sql1='create database 1903mysql character  set utf8'
# e.execute(sql1)
sql2='use 1903mysql'  #使用数据库
e.execute(sql2)
# sql3='create table studentinf (`ID` varchar(20),`NAME` varchar(30),SEX VARCHAR(5),`age` varchar(10))' #创建一张表
# e.execute(sql3)
#sql4='drop database 1903博文测试' #删除指定数据库
#e.execute(sql4)
#sql5="insert into studentinf value('1','张三','男','19')"#插入数据
#e.execute(sql5)
a=(('2','李四','男','23'),('3','李丽','女','24'),('4','晓芳','女','27'))
for i in a:
  sql6=f"insert into studentinf value {i} "#插入多条数据
  e.execute(sql6)
#sql7="update studentinf set id='001' where id='1'"
#e.execute(sql7)
#连接保存数据操作
''' 
a:找到连接
b:使用commit() --->保存数据到数据库
                                '''
d.commit()


