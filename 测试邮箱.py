#！/usr/bin/python
#-*-c0ding:utf-8-*-
#！/usr/bin/python
#-*-c0ding:utf-8-*-
import  smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# 第一步 服务器信息
mail_host='smtp.163.com'
# 2 用户信息
mail_user='17629759472@163.com'
#3 授权码
mail_pass='666888yx'
# 4 设置服务器端口号
mail_port=465
# #发送信息
# 4邮箱发送方地址
sender='17629759472@163.com'
# 5接收方地址  可以多个
receivers=['15206265349@163.com']
# 6 邮件正文
# 设置邮件主题
subject='python邮件测试'
#7 设置正文
content='大武汉的客户'
# 8 (       )三个参数：第一个为文本内容，第二个：plain 设置文本格式 ，第三个：utf-8  设置编码
message=MIMEText(content,'plain','utf-8')
# 9 发送邮件的过程
#第一步：添加发送者头部
message['From']=Header(sender)
# 第二步：添加接受者头部   转成字符串
message['To']=Header(str(';'.join(receivers)))
#第三步：添加邮箱主题
message['Subject']=Header(subject)
#链接邮箱服务器发送邮件
# 第一步：登录邮箱
s=smtplib.SMTP_SSL(host=mail_host,port=mail_port)
#第二步：输入账号，密码
s.login(mail_user,mail_pass)
# 第三步 发送邮件
s.sendmail(sender,receivers,message.as_string())
print('success')
#第四步：退出登录
s.close()