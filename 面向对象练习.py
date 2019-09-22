#！/usr/bin/python
#-*-c0ding:utf-8-*-
class dog(object):
    goutui=4 #类属性
    def __init__(self,maose,shengao,pinzhong,tizhong):#初始化方法
        self.maose=maose
        self.shengao=shengao
        self.pinzhong=pinzhong
        self.tizhong=tizhong
    def eat(self):  #对象属性
        print(f'{self.pinzhong},饿了要吃人^.^')
    def drink(self):
        print(f'{self.pinzhong},渴了要喝人肉仙汤')
    def run(self):
        print(f'{self.pinzhong},挨打了要飞天')
    def jiao(self):
        print(f'{self.pinzhong},遇到生人要咬死他')
    def info(self):
        print(f'狗狗的毛色为{self.maose},狗狗的身高{self.shengao},狗狗的品种为{self.pinzhong},狗狗的体重{self.tizhong}')
d=dog('灰色','140cm','藏獒','50kg')
d.eat()
d.drink()
d.run()
d.jiao()
d.info()
#面向对象图书管理系统练习
# 书：书名，作者，状态，位置
# 管理系统：
class Book(object):
    def __init__(self, name, author, status, bookindex):
        self.name = name
        self.author = author
        self.status = status
        self.bookindex = bookindex
    def __str__(self):
        if self.status == 1:
            stats = '未借出'
        elif self.status == 0:
            stats = '已借出'
        else:
            stats = '状态异常'
        return '书名: 《%s》 作者: %s 状态: <%s> 位置: %s' \
               % (self.name, self.author, stats, self.bookindex)
class BookManage(object):
    books = []
    def start(self):
        self.books.append(Book('python', '龟叔', 1, 'CP0001'))
        self.books.append(Book('c', '丹尼斯，瑞查恩', 1, 'CP0002'))
        self.books.append(Book('java', '帕特里克', 1, 'CP0003'))
        # 0:借出 1：存在
        # python 1
        # c 1
        # java 1
    def Menu(self):
        self.start()
        while True:
            print("""
                        图书管理系统
        1.查询图书
        2.增加图书
        3.借阅图书
        4.归还图书
        5.退出系统
        """)
            choice = input('请选择：')
            if choice == '1':
                self.showAllBook()
            elif choice == '2':
                self.addBook()
            elif choice == '3':
                self.borrowBook()
            elif choice == '4':
                self.returnBook()
            elif choice == '5':
                print('欢迎下次使用...')
                exit()
            else:
                print('请输入正确选择')
                continue
    def showAllBook(self):
        for book in self.books:
            print(book)
    def addBook(self):
        name = input('图书名称:')
        self.books.append(Book(name, input('作者:'), 1, input('存储位置:')))
        print('图书《%s》增加成功' % name)
    def checkBook(self, name):
        for book in self.books:
            if book.name == name:
                return book
        else:
            return None
    def borrowBook(self):
        name = input('借阅图书名称: ')
        ret = self.checkBook(name)
        print(ret)
        if ret != None:
            if ret.status == 0:
                print('书籍《%s》已经借出' % name)
            else:
                ret.status = 0
                print('书籍《%s》借阅成功' % name)
        else:
            print('书籍《%s》不存在' % name)
    def returnBook(self):
        name = input('归还图书名称:')
        ret = self.checkBook(name)
        if ret != None:
            if ret.status == 0:
                ret.status = 1
                print('书籍《%s》归还成功' % name)
                print(ret)
            else:
                print('书籍《%s》未借出' % name)
        else:
            print('书籍《%s》不存在' % name)
manager = BookManage()
manager.Menu()

