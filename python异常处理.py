# python 异常处理    错误不执行，继续运行执行错误下面的代码
"""
异常分类：
1 python 语法错误，缩进，缺少
2代码逻辑上的文体
########################
异常处理：
处理python代码中可能出现的错误
处理方法一
try:
    代码块1
except：
    代码块2
try 语句没有错误时 不执行except语句
try 语有错误时 执行except语句

except():可以指定异常的类型：
"""
# 例如
'''
try:
    a=1
    b=1/0
    print(d)
except:
    print('上层错误')
print('你好')
        '''
#try ...except ... finally
#try 语句存在错误，except,finally 语句都执行；try语句没错误则finally语句执行
try:
    a=1/0
except:
    print('try 语句内有bug')
finally:
    print('finally语句被执行')

#try ...excpet ...else
#try 语句存在错误，except语句执行,不执行else;
# try语句没错误则else语句执行
try:
    a = 1 / 0
except:
    print('try 语句内有bug')
else:
    print('finally语句被执行')