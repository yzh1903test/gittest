#！/usr/bin/python
#-*-c0ding:utf-8-*-
# import xlrd
# #操作Excle的xlrd读取Excle文件  xlwt 写入数据到Excle文件
# #1.打开Excle
# d=xlrd.open_workbook(filename='Python专用.xlsx')
# #2.选中一个子表   sheet1 sheet2
# #第一种选中表的方法
# table=d.sheets()[0]
# print(table)
# #第二种选中表的方法
# #d.sheet_by_index(0)
# #print(table)
# #3.获取数据
# a=table.row_values(0) #获取指定的整行数据，必须指定获取的行号
# print(a)
# #4.获取某一个单元格的值
# #"row()" 获取某一行  --->返回是一个列表
# #再通过列表的索引获取到元素  --->.value 获取具的值
# print(table.row(0)[0].value)
# 5.先获取一列 "col()" --->返回一个列表
# #再通过列表的索引获取到元素  --->.value 获取具的值
# print(table.col(0)[1].value)
# #6.通过行，列索引获取具体单元格的值
# print(table.cell(0,2).value)
# #7.获取行数，列数
# '''nrows:获取行数
#    ncols:获取列数  '''
# print(table.nrows)
# print(table.ncols)
# #8.如何获取所有行数据
# n=table.nrows
# for i in range(n):
#     data=table.row_values(i)
#     print(data)
# #9.如何获取所有列数据
# m=table.ncols
# for j in range(m):
#     data_1=table.col(j)
#     print(data_1)
# #10.如何获取文件中所有的表名
# print(d.sheet_names())

#面向对象之定义一个类：
#1.可以打开不同的Excle文件
#2.按照行读取任意数据2~4
#3.读取指定单元格的数据0,4
#4.按照列读取任意列数据
#5.指定某个表格的数据
# import xlrd
# #任意打开不同的Excle文件
# class Excel(object):
#     def __init__(self, name, n):
#         # 对象属性
#         self.name = name  # Excel文件名
#         self.n = n  # 表格
#         # 局部变量
#         # d = xlrd.open_workbook(filename=self.name)
#         self.d= xlrd.open_workbook(filename=self.name)
#         # 打开某一张表
#         self.table = self.d.sheet_by_index(self.n)
#     # 读取任意行数据
#     def read_row_data(self):
#         a = int(input("输入查询的第一个行号:"))
#         b = int(input("输入查询的第二个行号:"))
#         if a > b:
#             if a > self.table.nrows:
#                 print("超出查询范围")
#                 return None
#             else:
#                 for i in range(b, a + 1):
#                     print(self.table.row_values(i))
#         else:
#             if b > self.table.nrows:
#                 print("超出查询范围")
#                 return None
#             else:
#                 for i in range(a, b + 1):
#                     print(self.table.row_values(i))
#
#     # 读取任意行数据
#     def read_col_data(self):
#         a = int(input("输入查询的第一个列号"))
#         b = int(input("输入查询的第二个列号"))
#         if a > b:
#             if a > self.table.ncols:
#                 print("超出查询范围")
#                 return None
#             else:
#                 for i in range(b, a + 1):
#                     print(self.table.col_values(i))
#         else:
#             if b > self.table.ncols:
#                 print("超出查询范围")
#                 return None
#             else:
#                 for i in range(a, b + 1):
#                     print(self.table.col_values(i))
#
#     # 读取任意单元格
#     def read_cell_data(self):
#         a = int(input("输入要查询的单元格的行号"))
#         b = int(input("输入要查询的单元格的列号"))
#         print(self.table.cell(a, b).value)
#
#     # 定义主函数
#     def main(self):
#         print("1:查询任意列数据\t2:查询任意行数据\t3:查询任意单元格数据\t4:退出")
#         while True:
#             chose = input("输入你的选择:")
#             if chose == '1':
#                 self.read_col_data()
#             elif chose == '2':
#                 self.read_row_data()
#             elif chose == '3':
#                 self.read_cell_data()
#             elif chose == '4':
#                 break
#             else:
#                 print("不支持此功能")
# if __name__ == '__main__':
#     e = Excel('Python专用.xlsx', 0)
#     e.main()

# import  xlwt
# a = [
#     ["序号", "名字", "年龄", "性别"],
#     [1, "张三", 20, "男"],
#     [2, "李四", 19, "男"],
#     [3, "王五", 18, "女"],
#     [4, "赵信", 16, 	"女"]
# ]
# #1.新建一个Excle文件
# #"xlwt.Workbook()"
# d=xlwt.Workbook()
# #2.新建一个Excle表， add_sheet(工作表名称)，表名必填
# table=d.add_sheet("表一")
# #3.写入数据到Excle表  一次只能写入一个单元格
# #table.write(0,0,"张三")#行号，列号，写入数据值
# #4.保存Excle文件
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         table.write(i,j,a[i][j])

# d.save('bbb.xls') #"save(Excle文件名)"

#面向对象Excle操作
import xlwt
class read(object):
    f = open(file='a.txt', mode='r',encoding='utf-8')
    d=f.read()
    print(d)
    print()

