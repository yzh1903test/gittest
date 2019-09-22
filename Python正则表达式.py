#！/usr/bin/python
#-*-c0ding:utf-8-*-
#Python 正则表达式 re模块 正则模块 只能操作字符串
import re
#1."." 代表匹配除了换行符\n以外的任意一个字符
s='1111123123456'
#"search(参数1，参数2)" 搜索 参数1：已经编译好的正则；参数2：要匹配的字符串
#写正则的步骤：
'''
NO1.编译正则 re.compile(r'.') r1代表编译好的正则表达式
r1=re.compile(r'.')
NO2.执行正则表达式
re.search(r1,s)
'''
r1=re.compile(r'5.')
re.search(r1,s)
print(re.search(r1,s))
#2."*" 代表匹配*号前面的字符0次或多次
r2=re.compile(r'123*')
re.search(r2,s)
print(re.search(r2,s))
#3."+" 代表匹配+号前面字符1次或者多次
r3=re.compile(r'3+')
re.search(r3,s)
print(re.search(r3,s))
#4."?" 代表匹配?前面字符0次或1次
r4=re.compile(r'1?')
re.search(r4,s)
print(re.search(r4,s))
#5."$" 代表匹配以某个字符结尾
r5=re.compile(r'6$')
re.search(r5,s)
print(re.search(r5,s))
#6."^" 代表匹配以某个字符开头
r6=re.compile(r'^1')
re.search(r6,s)
print(re.search(r6,s))
#7."{m}" 代表匹配花括号字符m次
r7=re.compile(r'1{3}')
re.search(r7,s)
print(re.search(r7,s))
#8."{m,n}" 代表匹配花括号内字符最少m次，最多n次
r8=re.compile(r'1{1,5}')
re.search(r8,s)
print(re.search(r8,s))
#"[abc]" 代表匹配中括号内字符任意一个字符
r9=re.compile(r'3[456]')
re.search(r9,s)
print(re.search(r9,s))
#10.[abc]. 代表匹配中括号内所有字符
r10=re.compile(r'1[23].')
re.search(r10,s)
print(re.search(r10,s))

#"\d" 代表0-9 "\D"代表除了0-9以外的任意字符
# "\s"代表空白字符
# unicod编码空白字符 \t \n \f \r \v "\V" 代表除了空白字符以外的任意字符
#正则过滤手机号
a="'17629759472','18211917896','15263978956','19679549633','13598491945','18837912735'"
r11=re.compile(r'^1[0-9]{10}')

re.search(r11,a)
print(re.match(r11,a))

#贪婪与非贪婪
'''
贪婪指的是尽可能匹配更多的字符
'''
'''
非贪婪指的是匹配到符合正则规则的字符，就停止匹配
'''
#sub(参数1,参数2,参数3) 替换  参数1：正则 参数2：新的字符串 参数3：被更改的字符串
# "group" 将获匹配的内容取出
#贪婪模式
URL="https://www.baidu.comhttps://www.jd.com"
r12=re.compile(r'\.(.*)\.')
res_1=re.search(r12,URL).group()
re.search(r12,URL)
print(re.search(r12,URL))
b=re.sub(r'\.','',res_1)
print(b)
#非贪婪模式
URL="https://www.baidu.comhttps://www.jd.com"
r12=re.compile(r'\.(.*?)\.')
res_1=re.search(r12,URL).group()
re.search(r12,URL)
print(re.search(r12,URL))
c=re.sub(r'\.','',res_1)
print(c)

#"re.findall" 返回列表，每个元素为字符串 匹配所有符合正则规则的结果
URL="https://www.baidu.comhttps://www.jd.com"
r13=re.compile(r'\.(.*?)\.')
res_2=re.findall(r13,URL)
print(res_2)


