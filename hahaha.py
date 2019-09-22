# -*- coding: utf-8 -*- 

# @Time : 2019/7/23 下午3:27 

# @Author : 废柴 

# @Project: teach

# @FileName : hahaha.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================



# 图书管理系统 类
"""
1.查询图书
2.增加图书
3.借阅图书
4.归还图书
5.退出系统

书：书名，作者，状态
"""
# 导入pymysql模块
import pymysql
# **kwargs
# 第一步：与mysql建立连接  connect()：建立连接
d = pymysql.connect(
    host='127.0.0.1', # 数据库所在的主机IP地址/域名【云服务器--mysql数据库】
    port=3306,  # mysql的端口号
    user="root", # mysql的用户名
    password="MySql@941029",  # mysql的用户密码，授权密码
    charset="utf8", # mysql数据的编码方式
    database="zouxin",  # 指定数据库，不写这个参数，默认使用所有的数据库
)
# 第二步：创建一个游标，类似于mysql进入命令行模式 mysql> select * from xx;
e = d.cursor()

# 第三步：写sql语句
sql = 'show databases'

# 第四步：执行sql语句 execute(放入需要执行的sql语句): 作用就是执行sql
# executemany(sql语句) # 执行多条sql语句
data = e.execute(sql)

# 第五步：查询具体结果

"""
a：先找到游标
b：再使用fethchxx()
"""
s = e.fetchmany(3)
print(s)

"""
fetchall() # 获取执行sql之后的所有结果
fetchone() # 获取执行sql之后的第一个结果
fetchmany(数字) # 3 获取执行sql之后的前三条
"""

# 创建一个库
# sql1 = "create database zouxin character set utf8"
#
# e.execute(sql1)

# # 创建一个表
# sql2 = "create table user (id varchar(20), name varchar(30), age int(30))"
# e.execute(sql2)

# e.execute('desc user')
# print(e.fetchall())

# 数据插入


a = (('2', '王二', 16), ('3', '哈哈', 16))


for i in a:

    sql3 = f"insert into zouxin.user value {i}"

    e.execute(sql3)

# 保存操作
"""
a: 找到连接
b: 使用commit() ---> 保存数据到数据库
"""
d.commit()

# # 更新操作
# sql5 = "update zouxin.user set name='good' where id = '1'"
# e.execute(sql5)
#
# d.commit()









"""
python模块（module）
自我包含并且有组织的代码片段为模块。
表现形式为：写的代码保存为文件。这个文件就是一个模块。sample.py 其中文件名smaple为模块名字。
python包（package）
包是一个有层次的文件目录结构，它定义了由n个模块或n个子包组成的python应用程序执行环境。通俗一点：包是一个包含__init__.py 文件的目录，该目录下一定得有这个__init__.py文件和其它模块或子包。
python库（lib）
是参考其它编程语言的说法，就是指python中的完成一定功能的代码集合，供用户使用的代码组合。在python中是包和模块的形式。

一般按照API的惯例来设计库。
应用程序接口（英语：Application Programming Interface，简称：API），又称为应用编程接口，就是软件系统不同组成部分衔接的约定。由於近年來软件的规模日益庞大，常常需要把复杂的系统划分成小的组成部分，编程接口的设计十分重要。程序设计的实践中，编程接口的设计首先要使软件系统的职责得到合理划分。良好的接口设计可以降低系统各部分的相互依赖，提高组成单元的内聚性，降低组成单元间的耦合程度，从而提高系统的维护性和扩展性。

python框架
Django，flask这些是框架。
框架（framework）是一个基本概念上的结构，用于去解决或者处理复杂的问题。这个广泛的定义使用的十分流行，尤其在软件概念。框架也能用于机械结构。
"""

