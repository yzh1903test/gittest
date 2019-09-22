#/user/bin/python
#-*-c0ding:utf-8-*-
# a=abs(-6) #绝对值
# print(a)
# b=round(16.88,1) #四舍五入，保留一位
# print(b)
# c='我爱我'
# d='的宝贝'
# print(c+d)
# print('A'*3)
# print('YanZhaoHui'[3])
# print('yanzhaohui'[:-1])
# print('123abc123'.strip('21'))
# print('apple'.startswith('e'))
# print('HuaWei'.endswith('ei'))
# print('Honor'.find('o'))
# a=[6,7,7,8,8,9]
# set(a)
# print(a)
# #定义列表
# a=[[1,],'zifu',68,(1,6),{5,9},{'a':'弟弟'}]
# print(a.remove(68))
# s=[1,5,6,7]
# s.sort()
# print(s)
# x=[5,8,9,6,'abcd','daw','数字图像']
# for i,j in  enumerate(x):
#     print(i)
#     print(j)

a=['香蕉','菠萝','提子','萝卜']
b=[30,50,20,25,40]
k=[90,35,20,70,26]
print('商品编号   \t商品名\t\t\t单价')
for i ,j in enumerate(a):
    print('{}\t\t\t{} \t\t\t{}'.format(i,j,b[i]))
c=int (input('请输入商品编号：'))
if  0<=len(a):
    d=int(input('请输入购买数量:'))
    if 0<(d):
        e=input('是否使用会员?(yes or no)')
        if e=='yes':
            f=input('请输入会员卡号:')
            if f in ['123456','666666']:
                print('应付金额为{}元'.format(b[int(c)]*int(d)*0.95))
            else:
                print('会员卡号输入错误!')
        elif e=='no':
            print('应付金额为{}元'.format(b[int(c)] * int(d)))
        else:
            print('输入无效,只能输入“yes”或"no"')
    else:
        print('数量输入错误!')
else:
    print('商品号输入错误!')


