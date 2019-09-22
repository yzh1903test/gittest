#！/usr/bin/python
#-*-coding:utf-8-*-
import xlrd
import pymysql
#打开数据所在的工作簿，以及选择存有数据的工作表
book=xlrd.open_workbook('test.xlsx')
sheet=book.sheet_by_name('Sheet1')
# 建立一个MySQL
conn=pymysql.connect(
        host='localhost',
        user='root',
        passwd='446794',
        database='atxttest',
        port=3306,
        charset='utf8'
        )
# 获得游标4
cur=conn.cursor()
# 创建插入SQL语句
# sql1='create table student_test(`name` char(15),`sex` char(6),`minzu` char(6),`danwei` char(100),`phone` char(20),`house_number` int(10))'
# cur.execute(sql1)
sql2='insert into student_test (name,sex,minzu,danwei,phone,house_number) values (%s,%s, %s, %s, %s, %s)'
# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
for i in range(1, sheet.nrows):
      name= sheet.cell(i,1).value
      sex= sheet.cell(i,2).value
      minzu= sheet.cell(i,3).value
      danwei= sheet.cell(i,4).value
      phone= sheet.cell(i,5).value
      house_number= sheet.cell(i,6).value
      values=(name,sex,minzu,danwei,phone,house_number)
      # 执行sql语句
      cur.execute(sql2,values)
cur.close()#断开sql语句
conn.commit()#断开mysql连接
conn.close()#保存关闭b
# rows=str(sheet.nrows)#行
# cols=str(sheet.ncols)#列
# print ("导入"+rows+" 行 "+cols+"列数据到MySQL数据库!")