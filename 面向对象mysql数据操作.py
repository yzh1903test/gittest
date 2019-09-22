#！/usr/bin/python
#-*-c0ding:utf-8-*-
import pymysql
class mysqld(object):
    def __init__(self,host,port,user,password,charset):
        self.connect = pymysql.connect(
            host=host,  # 数据库所在的主机ip地址/域名【云服务器---mysql数据库】
            port=port,  # mysql 端口号
            user=user,  # mysql用户名
            password=password,  # 密码
            charset="utf8",  # 编码方式 默认utf8
    # database = "库名"  # 指定数据库，不写，默认所有数据库
        )
        self.s = self.connect.cursor()

    def create_database(self):
        sql1='create database atxttest character set utf8'
        self.s.execute(sql1)

    def create_table(self):
        sql12 = 'use atxttest'
        self.s.execute(sql12)
        # sql2="create table jobinfo (`id` char(10),`qiye` char (100),`job` char (100),`url` varchar(500),`leixing` varchar(100),`status` varchar(50),`guimo` varchar(200),`address` varchar(500),`jingyan` char(100),`xueli` char(200))"
        # self.s.execute(sql2)

    def open_file(self):
        self.e = []
        self.a = open(file='a.txt', encoding='utf-8')
        self.b = self.a.readlines()
        # print(b)
        for i in self.b:
            self.c = i.replace('\n', '').replace("'", '').replace('(', '').replace(';', '').replace(')', '')
            self.d = self.c.split(',')
            self.e.append(self.d)
        f = len(self.e)
        self.e.pop(f - 1)
        print(self.e)
    def insert_into(self):
        for j in self.e:
          sql3='insert into tmd value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
          self.s.execute(sql3,(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8],j[9]))

    def baocun(self):
        self.connect.commit()
m=mysqld('localhost',3306,'root','446794','utf8')
m.create_table()
m.open_file()
m.insert_into()
m.baocun()
