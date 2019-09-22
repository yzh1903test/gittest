#！/usr/bin/python
#-*-c0ding:utf-8-*-
import  smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
class   youjian(object):
    def __init__(self,mail_host,mail_user,mail_pass,mail_port,sender,receivers):
        self.mail_host=mail_host
        self.mail_user=mail_user
        self.mail_pass=mail_pass
        self.mail_port=mail_port
        self.senfer=sender
        self.receivers=receivers
    def   fa(self):
        mail_host=self.mail_host
        mail_user=self.mail_user
        mail_port=self.mail_port
        sender= self.senfer
        receivers=self.receivers
        a1=input('邮件主题:')
        subject =a1
        a=input('邮件正文:')
        content =a
        message = MIMEText(content, 'plain')
        message['From'] = Header(sender)
        message['To'] = Header(str(';'.join(receivers)))
        message['Subject'] = Header(subject)
        s = smtplib.SMTP_SSL(host=self.mail_host, port=self.mail_port)
        s.login(self.mail_user, self.mail_pass)
        s.sendmail(sender, receivers, message.as_string())
        print('success')
        s.close()

w=youjian('smtp.163.com','176297559472@163.com','666888yx',465,'15206265349@163.com',receivers=['17629759472@163.com'])
w.fa()