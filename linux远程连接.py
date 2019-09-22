#！/usr/bin/python
#-*-c0ding:utf-8-*-
import paramiko #用于远程连接linux 文件下载，上传，服务开启等
#面向过程  ssh协议连接，可以执行linux内命令
#第一步：创造一个ssh的客户端、对象 ssh协议
# C=paramiko.SSHClient()
# # #第二步：信任Linux主机,类似xshell第一次连接的保存信息 自动添加密文
# C.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# #3.通过客户端连接远程Linux主机
# C.connect(hostname='192.168.10.85',
#           port=22,
#           username='root',
#           password='123456')
# #4.执行Linux命令 exec_command('要执行的命令')
# '''
# stdin:输入 ls -al
# stdout:输出结果
# stderr:错误信息
#                    '''
# stdin,stdout,stderr=C.exec_command('ls -al')
# print(stdout.read().decode())  #decode() 把***编译成***
#文件的下载与上传 Transport()  类似于ftp服务器  参数：包含IP地址与端口号的元祖
#Ftp=paramiko.Transport(('192.168.10.85',22))
#建立与远程Linux服务器的链接
#Ftp.connect(username='root',password='123456')
#创建一个类似Ftp的客户端 paramiko.SFTPClient.from_transport(Ftp)
#sftp=paramiko.SFTPClient.from_transport(Ftp)
# #下载远程文件  get(参数1,参数2) 参数1：远程文件/参数2：本机文件
# x1='/home/n的阶乘之和.sh'
# x2=r'D:\PycharmProjects\untitled\n的阶乘之和.sh'
# sftp.get(x1,x2)
# #上传远程文件  将本机文件上传至linux   put(参数1,参数2) 参数1：本机文件/参数2：远程主机文件名
# y1=r'D:\PycharmProjects\untitled\python笔记.py'
# y2='/home/python笔记.txt'
# sftp.put(y1,y2)
#断开连接
#Ftp.close()


#面向对象Linux远程
'''
1.可执行Linux命令
2.可以下载上传文件
3.不同的对象、ip、用户名和密码不一样时都可以用
    '''
class sshlinux(object):
    c=paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    def __init__(self,h,p,u,pd):
        self.Ftp=paramiko.Transport((h,p))
        self.Ftp.connect(username=u, password=pd)
    def mlling(self):
        stdin, stdout, stderr = self.c.exec_command('')
        print(stdout.read().decode())
    def ftpservice(self,x1,x2):
        sftp = paramiko.SFTPClient.from_transport(self.Ftp)
        sftp.get(x1,x2)
        sftp.put(x1,x2)
        self.c.close()
l=sshlinux('192.168.10.108',22,'root','123456')
