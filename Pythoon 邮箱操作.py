# #！/usr/bin/python
# #-*-coding:utf-8-*-
# #Python 发送电子邮件
# #使用内置邮件模块 smtplib email
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
# #设置服务器的信息
# mail_host='smtp.163.com'
# #用户信息
# mail_user='17629759472@163.com'
# #用户授权码
# mail_pass='666888yx'
# #邮件服务器的端口号
# mail_port=465
# #邮件发送方的地址
# sender='17629759472@163.com'
# #邮件接收方的地址
# receivers=['18317822978@163.com']
# # #>>>设置邮件正文
# # #邮件主题
# subject='python电子邮件'
# # #正文
# # content='python学的什么玩意儿！最后啥也不会啊！'
# # #MIMEText正文邮件转邮件格式 "content":文本内容;"plain":文本的格式
# # message=MIMEText(content,'plain','utf-8')
# # #>>>发送邮件
# # #NO1.添加发送者头部信息
# # message['From']=Header(sender)
# # #NO2.添加接收者信息
# # message['TO']=Header(str(';'.join(receivers)))
# # #NO3.添加邮件主题
# # message['Subject']=Header(subject)
# # #>>>连接服务器并发送邮件
# # #NO1.登录邮件邮箱
# # s=smtplib.SMTP_SSL(host=mail_host,port=mail_port)
# # #NO2.输入账号密码
# # s.login(mail_user,mail_pass)
# # #NO3.发送邮件
# # s.sendmail(sender,receivers,message.as_string())
# # print('success!')
# # #NO4.退出登录
# # s.close()
# # #s.quit()
#
# #带附件邮箱发送  将正文及附件添加到邮件里
# message=MIMEMultipart()
# #NO1.添加发送者头部信息
# message['From']=Header(sender)
# #NO2.添加接收者信息
# message['TO']=Header(str(';'.join(receivers)))
# #NO3.添加邮件主题
# message['Subject']=Header(subject)
# #准备要发送的html正文
# with open(file='操蛋邮件.html',mode='r',encoding='utf-8',errors='ignore')as f:
#     content=f.read()
# #设置HTML格式
# p1=MIMEText(content,'html','utf-8')
# #准备要发送的附件
# with open(file='hello.txt',mode='r',encoding='utf-8',errors='ignore')as f1:
#     d=f1.read()
# p2=MIMEText(d,'plain','utf-8')
# #将文本转为二进制流
# p2['Content-Type'] = 'application/octet-stream'
# #将附件添加文件名
# p2['Content-Disposition'] = "attachment;filename='hello.txt'"
# #添加一个照片
# with open(file='0.jpg',mode='rb')as f:
#  p3=MIMEImage(f.read())
# #将图片转为二进制
# p3['Content-Type'] = 'application/octet-stream'
# #将附件添加一个名
# p3['Content-Disposition'] = "attachment;filename='0.jpg'"
# #将各个附件添加到邮件里
# message.attach(p1)
# message.attach(p2)
# message.attach(p3)
# #发送邮件
# #>>>连接服务器并发送邮件
# # #NO1.登录邮件邮箱
# s=smtplib.SMTP_SSL(host=mail_host,port=mail_port)
# # #NO2.输入账号密码
# s.login(mail_user,mail_pass)
# # #NO3.发送邮件
# s.sendmail(sender,receivers,message.as_string())
# print('success!')
# # #NO4.退出登录
# s.close()
# import re
# with open(file='a.txt',mode='r',encoding='utf-8') as f:
#     b = f.read()
#     c = b.split('\n')
#     d = len(c)
#     r1 = re.compile(r'#(.*?)')
#     g = re.findall(r1, b)
#     j = len(g)
#     r2 = re.compile(r'$')
#     h = re.findall(r2, b)
#     k = len(h)
# print(f"共有{d}行，空行有{k}行，单行注释有{j}行，去除空行和单行{d-j-k}")
s = 0
a = input("请输入：")
b = a.split('-')
print(b)
if int(b[0]) % 400 == 0 or (int(b[0]) % 4 ==0 and int(b[0]) % 100 != 0):
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(int(b[1])- 1):
        s += day[i]
    s += int(b[2])
    a = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
    c = s % 7
    print(f"{b[0]}年是闰年,是一年的第{s-1}天，今天是{a[c]}")
else:
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(int(b[1])- 1):
        s += day[i]
    s += int(b[2])
    a = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    c = s % 7
    print(f"{b[0]}年不是闰年,是一年的第{s-1}天，今天是{a[c]}")