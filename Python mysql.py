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
    charset="utf8" # mysql数据的编码方式
    # database="库名",  # 指定数据库，不写这个参数，默认使用所有的数据库
)
#3.创建一个游标;mysql进入命令行模式
e=d.cursor()
#4.写SQL语句
sql='show databases'
#5.执行Sql语句  "execute"放入传入的sql语句，执行sql语句
data=e.execute(sql)
print(data)
#查询具体结果
print(e.fetchall())#查询执行sql后的所有结果
#e.fetchmany()#查询执行sql后的指定结果
#e.fetchone()#查询执行sql后的第一个结果