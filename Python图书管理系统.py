#！/usr/bin/python
#-*-c0ding:utf-8-*-
#  图书管理
class Book(object):
    books = [
        ['三国演义', '罗贯中', '1', 'A区'],
        ['西游记', '吴承恩', '1', 'B区'],
        ['水浒传', '施耐庵', '1', 'C区'],
        ['红楼梦', '曹雪芹', '1', 'D区'],
    ]
    def __init__(self, name, author, status, weizhi):
        # 对象属性
        self.name = name
        self.author = author
        self.status = status
        self.weizhi = weizhi
    # 展示图书
    def show(self):
        # 展示图书并编号
        print(f"库存书籍")
        print(f"图书编号\t\t\t书名\t\t\t作者\t\t\t状态\t\t\t区域")
        for i, j in enumerate(self.books):
            print(f"{i}\t\t\t\t{j[0]}\t\t{j[1]}\t\t{j[2]}\t\t\t{j[3]}")
            # print(i, j)
    # 实例方法
    def add_book(self):
        # 添加书籍
        self.books.append([self.name, self.author, self.status, self.weizhi])
        # 添加之后的书籍
        self.show()
    # 借出图书
    def borrow_book(self):
        bianhao = int(input("请输入书籍编号:"))

        if bianhao in range(len(self.books)):
            if self.books[bianhao][2] == '1':
                print("书可以借出")
                self.books[bianhao][2] = '0'
                print(self.books)
            else:
                print("书已被借出")
        else:
            print("书库不存在此书")
    # 还书
    def huan_book(self):
        book_name = input("请输入要归还的书名:")
        for i in self.books:
            if book_name in i[0]:
                i[2] = '1'
                print('归还成功')

            else:
                print("此书不属于本图书馆")

    def main(self):  # main --> 主要的
        while True:
            # 展示已有的所有图书
            self.show()
            # 展示借出、归还、添加图书、退出的功能
            print("选择你要的功能")
            print("1：借出")
            print("2：归还")
            print("3：添加")
            print("4：退出")
            chose = input("请输入你的操作编号:")
            if chose == '1':
                self.borrow_book()
            elif chose == '2':
                self.huan_book()
            elif chose == '3':
                self.add_book()
            elif chose == '4':
                print("欢迎下次再来")
                break
            else:
                print("请输入正确操作编号:")
b1 = Book('飘', '简', '1', 'E区')
b1.main()
#面向对象图书管理系统
#书：书名；作者；状态；位置
#管理系统
class book(object):
    def __init__(self,bookname,author,status,bookindex):
        self.bookname=bookname
        self.author=author
        self.status=status
        self.bookindex=bookindex
    def __str__(self):#魔法方法（自动将对象属性的值输出，输出的是一个字符串）
        if self.status==1:
           stats='未借出'
        elif self.status==0:
            stats='已借出'
        else:
            stats='状态异常'
        return '书名：《%s》 作者:%s 状态:<%s> 位置:%s '\
               %(self.bookname,self.author,stats,self.bookindex)
class bookmanage(object):
    books=[]
    def start(self):
        self.books.append(book('Python入门基础','龟叔叔',0,'ITaox0301'))
        self.books.append(book('java掉头发神器','头发叔叔',1,'ITaox0302'))
        self.books.append(book('C语言基础','头发妈妈',1,'ITaox0300'))
        self.books.append(book('中华上下5000年','戴丽名',0,'HISaox01001'))
        self.books.append(book('雨后初晴','刘坚强',1,'eduaox01002'))
        self.books.append(book('沙漠里的骆驼','蒋蒋', 0,'wenaox0100X'))
    def Menu(self):
        self.start()
        while True:
            print('''          图书管理系统菜单
                  1.查询图书
                  2.增加图书
                  3.借阅图书
                  4.归还图书
                  5.退出系统
                     '''    )
            choice=input('请选择:')
            if choice=='1':
                self.showAllbooks()
            elif choice=='2':
                self.addbooks()
            elif choice=='3':
                self.borrowbook()
            elif choice=='4':
                self.returnbook()
            elif choice=='5':
                print('系统退出，欢迎下次使用！')
                exit()
            else:
                print('请输入正确的选择')
                continue
    def showAllbooks(self):
        for book in self.books:
            print(book)
    def addbook(self):
        name=input('添加图书名称:')
        self.books.append(book(name,input('作者:'),1,input('存储位置：')))
    def checkbook(self,bookname):
        for book in self.books:
            if book.bookname==bookname:
                return book
            else:
                return None
    def borrowbook(self):
        name=input('借阅图书名称：')
        borrow=self.checkbook(name)
        print(borrow)
        if borrow!=None:
            if borrow.status==0:
                print('书籍《%s》已经借出'%name)
            else:
                borrow.status=0
                print('书籍《%s》借阅成功'%name)
        else:
            print('书籍《%s》不存在'%name)
    def returnbook(self):
        name=input('归还图书名称:')
        borrow=self.checkbook(name)
        if borrow!=None:
            if borrow.status==0:
                borrow.status=1
                print('书籍《%s》归还成功'%name)
                print(borrow)
            else:
                print('书籍《%s》未借出'%name)
        else:
            print('书籍《%s》不存在' % name)
m=bookmanage()
m.Menu()


