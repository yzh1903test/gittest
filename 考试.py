#九九乘法表
# for a in range(1,10):
#     for b in range(1,a+1):
#         print('%s*%s=%s'%(a,b,a*b),end=' ')
#     print()
###################################################
#将字符串转成整数
# a=input("请输入一个字符:")
# b= a[::-1]
# for i,j in enumerate(b):
#     for h in range(100):
#       if str(h) == j:
#        b = h * (100 ** i)
# print(a)
# print(type(b))
########################################################3
#创建文件目录删除
# import  os
# # a=os.mkdir('BBB')
# # a1 = open(file='BBBB.txt',mode='w', encoding='utf-8')
# # a1.write('hello world')
# os.remove('BBBB.txt')
# os.rmdir('AAAAAAAA')
##################################3
#连接数据库将666.txt文件写入数据库
# import  pymysql
# qq=[]
# q1=[]
# a=pymysql.connect(
#     host='192.168.10.65',
#     port=3306,
#     user='root',
#     password='654321',
#     charset='utf8',
#     database='a'
# )
# b1=a.cursor()
# b2='create table KK(`xiaoshuo` varchar(10000)) character  set utf8 '
# b1.execute(b2)
# a1=open(file='666.txt',encoding='utf-8')
# b=a1.readlines()
# q1.append(b)
# print(q1)
# # a2=(a1.read())
# # print(a2)
# # qq.append(a2)
# for i in q1:
#     b=(str(i))
# #     k=(str(i))
# #     q1.append(k)
# #     print(q1)
#     b3='insert into KK values(%s)'
#     b1.execute(b3,b)
# a.commit()

#爬取臭事百科的文字写到数据库
# import  requests
# import  re
# import  pymysql
# aa=[]
# a=pymysql.connect(
#     host='192.168.10.65',
#     port=3306,
#     user='root',
#     password='654321',
#     charset='utf8',
#     database='a'
#
# )
# a1=a.cursor()
# a2='create table aa(`xiaoshuo` varchar(10000)) character  set utf8 '
# a1.execute(a2)
# a4=requests.get(url='https://www.qiushibaike.com/text/')
# a5=a4.content.decode(encoding='utf-8')
# a6=re.compile(r'(.*?)<br/>')
# a7=re.findall(a6,a5)
# aa.append(a7)
# for  i  in  aa:
#     bb=(str(i))
#     b1='insert into  aa  values(%s)'
#     a1.execute(b1,bb)
#     a.commit()
######################################################################################################################
#连接liunx主机
# import paramiko
# client=paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(
#     hostname='192.168.10.120',
#     port=22,
#     username='root',
#     password='123456'
# )
# stdin, stdout, stderr=client.exec_command('ls -al')
# print(stdout.read().decode())
#################################################################3
# #发邮件
# import  smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
# mail_host='smtp.163.com'
# mail_user='15206265349@163.com'
# mail_pass='123456w'
# mail_port=465
# sender='15206265349@163.com'
# receivers=['18317822978@163.com']
# subject='python考试'
# content='陈无名发送'
# message=MIMEText(content,'plain','utf-8')
# message = MIMEMultipart()
# message['From'] = Header(sender)
# message['To'] = Header(str(";".join(receivers)))
# message['Subject'] = Header(subject)
# with open(file='AAA.html',mode='r',encoding='utf-8') as f:
#     content = f.read()
# p1 = MIMEText(content, 'html', 'utf-8')
# with open(file='666.txt', mode='r', encoding='utf-8') as f:
#     d = f.read()
# p2 = MIMEText(d, 'plain', 'utf-8')
# p2['Conntent-Type'] = 'application/octet-stream'
# p2['Content-Disposition'] = 'attachment;filename="666.txt"'
# with open(file='0.jpg',mode='rb') as f:
#     d = f.read()
# p3 = MIMEImage(d)
# p3['Conntent-Type'] = 'application/octet-stream'
# p3['Content-Disposition'] = 'attachment;filename="0.jpg"'
# message.attach(p1)
# message.attach(p2)
# message.attach(p3)
# s=smtplib.SMTP_SSL(host=mail_host,port=mail_port)
# s.login(mail_user,mail_pass)
# s.sendmail(sender,receivers,message.as_string())
# print('dfdfdfd')
# s.close()
###########################################################
#爬取boss直聘信息
# import  requests
# import random
# import re
# w1=[]
# w2=[]
# w3=[]
# a = [
#     "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
#     "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
#     "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
#     "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
#     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
#     "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
#     "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
#     "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
#     "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
#     "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
#     "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
#     "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
#     "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
#     "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
#     "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
#     "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
#     "UCWEB7.0.2.37/28/999",
#     "NOKIA5700/ UCWEB7.0.2.37/28/999",
#     "Openwave/ UCWEB7.0.2.37/28/999",
#     "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
#     # iPhone 6：
#     "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",]
# print(len(a))
# a1=random.randint(1,37)
# a2=(a[a1])
# w={"User-Agent":a2}
# # print(w)                                                                                                                          }
# x=requests.get(url='https://www.zhipin.com/job_detail/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&city=101010100&industry=&position=',headers=w)
# date=x.content.decode(encoding='utf-8')
# print(date)
# r1=re.compile(r'(.*?)<em class="vline"></em>')
# b=re.findall(r1,date)
# print(b)
##################################################################################
#将数据库数据写入excel表格中
# import  pymysql
# import  xlwt
# q=[]
# a=pymysql.connect(
#     host='192.168.10.65',
#     port=3306,
#     user='root',
#     password='654321',
#     charset='utf8',
#     database='ku'
#
# )
# a1=a.cursor()
# a2='select *  from  r'
# a1.execute(a2)
# a3=a1.fetchall()
# print(a3)
# for i in a3:
#     q.append(i)
#     a4=xlwt.Workbook()
# a5=a4.add_sheet('G')
# for e in range(len(q)):
#       for j in range(len(q[e])):
#         a5.write(e,j,q[e] [j])
# a4.save('1.xls')
##################################################
# 统计多少行
# import re
# with open(file='666.txt',mode='r',encoding='utf-8') as f:
#     b = f.read()
#     c = b.split('\n')
#     d = len(c)
#     r1 = re.compile(r'#(.*?)')
#     g = re.findall(r1, b)
#     j = len(g)
#     r2 = re.compile(r'$')
#     h = re.findall(r2, b)
#     k = len(h)
# print(f"共有{d}行，空行有{k}行，单行注释有{j}行，去除空行和单行有{d-j-k}")
#######################################################################################
#判断日期
# s = 0
# a = input("请输入时间：")
# b = a.split('-')
# print(b)
# if int(b[0]) % 400 == 0 or (int(b[0]) % 4 ==0 and int(b[0]) % 100 != 0):
#     day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     for i in range(int(b[1])- 1):
#         s += day[i]
#     s += int(b[2])
#     a = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
#     c = s % 7
#     print(f"{b[0]}年是闰年,是一年的第{s-1}天，今天是{a[c]}")
# else:
#     day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     for i in range(int(b[1])- 1):
#         s += day[i]
#     s += int(b[2])
#     a = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
#     c = s % 7
#     print(f"{b[0]}年是平年,是一年的第{s-1}天，今天是{a[c]}")










