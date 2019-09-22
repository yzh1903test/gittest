#！/usr/bin/python
#-*-c0ding:utf-8-*-
##连接数据库，查询结果写入数据到excel
import pymysql
import xlwt
def get_excel(file_excel):
    #建立连接
    conn= pymysql.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        passwd = "446794",
        db = "atxttest",
        charset = "utf8"
    )
    #建立游标
    cursor=conn.cursor()
    sql = "select * from student_tbl;"
    print("开始查询表！")
    #执行sql语句
    cursor.execute(sql)
    #获取查询到结果
    res=cursor.fetchall()
    print(res)
    w_excel(res)
#操作excel
def w_excel(res):
    book = xlwt.Workbook() #新建一个excel
    sheet = book.add_sheet('test1') #新建一个sheet页
    title = ['姓名','性别','民族','单位','电话','住房']
#写表头
    i = 0
    for header in title:
        sheet.write(0,i,header)
        i+=1
#写入数据
    for row in range(1,len(res)):
        for col in range(0,len(res[row])):
            sheet.write(row,col,res[row][col])
        row+=1
    col+=1
    book.save('test1.xls')
    print("导出成功！")
if __name__ == "__main__":
    file_excel = r"D:\Users\1903\untitled\test1.xls"
    get_excel(file_excel)