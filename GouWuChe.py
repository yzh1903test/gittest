#/user/bin/python
#-*-c0ding:utf-8-*-
s=['香蕉','菠萝','提子','萝卜']
p=[100,80,50,30]
k=[20,30,15,45]
Vnumber={'nu':'446794967','pass':'697844aee@$'}
print(f"商品编号\t\t\t商品名\t\t\t商品价格\t\t\t库存量")
for i,j in enumerate(s):
    print('{}    \t\t\t{} \t\t\t{}  \t\t\t'.format(i,j,p[i]),k[i])
while True:
    a=input('购买输入"y"，退出输入"n:')
    if a=='y':
        bianhao=int(input('请输入商品编号：'))
        price=int(input('请输入购买数量:'))
        huafei=p[bianhao]*price
        print(f'您购买的商品是:{s[bianhao]},购买数量为：{price},消费金额为：{huafei}')
        vip=input('会员请选择"v":')
        if vip=="v":
            ip=int(input('输入会员卡号：'))
            if ip in Vnumber.keys():
                password=int(input('输入会员卡密码：'))
                if password==Vnumber.values():
                   huafei *=0.95
                else:
                    print('请重新确认')
        else:
            print('抱歉你不是会员')
            print('遵敬的顾客您需要支付{}'.format(huafei))
        break
    elif a=='n':
        print('欢迎下次再来！')







