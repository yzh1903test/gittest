#！/usr/bin/python
#-*-c0ding:utf-8-*-
class commodity(object):
    def __init__(self, name, price, status, commodityindex):
        self.name = name
        self.price = price
        self.status = status
        self.commodityindex = commodityindex
    def __str__(self):
        if self.status >= 1:
            startus = '有库存'
        elif self.status == 0:
            startus = '无库存'
        else:
            startus = '系统出错'
            return '商品名称：《%s》 价格：%s  状态：<%s>  位置：%s' \
                    % (self.name,self.price,startus,self.commodityindex)
class Commodity(object):
    commodity = []
    def start(self):
        self.commodity.append(Commodity('薯条','10元',1,'AAA0001'))
        # AAA意为A层A区A货架 0001号商品
        self.commodity.append(Commodity('辣条','5元',1,'AAA0002'))
        self.commodity.append(Commodity('辣鸭脖','15元','AAA0003'))
    def Menu(self):
        self.start()
        while True:
            print("""
                        超市货物管理系统
            1.查询商品
            2.转移商品
            3.售出商品
            4.商品补充
            5.退出系统
            """)
            chose = input('选择系统服务：')
            if chose == '1':
                self.show_all_commodity()
            elif chose == '2':
                self.Transfer_commodity()
            elif chose == '3':
                self.workoff_commodity()
            elif chose == '4':
                self.supplement_commodity()
            elif chose == '5':
                print('欢迎下次光临')
                exit()
            else:
                print('服务不存在')
                continue
    def show_all_commodity(self):
        for commodity in self.commodity:
            print(commodity)
    def Transfer_commodity(self):
        name = input('转移商品名称：')
        self.commodity.append(Commodity(name,input('价格：'),1,input('转移位置到：')))
        def checkBook_commodity(self, name):
            for commodity in self.commodity:
                if commodity.name == name:
                    return name
                else:
                    return None
        result = self.checkBook_commodity(name)
        if result != None:
            if result.startus == 0:
                print('商品【%s】已清空' % name)
            else:
                result.startus = 0
                print('商品《%s》转移成功')
    def checkBook_commodity(self,name):
        for commodity in self.commodity:
            if commodity.name == name:
                return name
            else:
                return None
    def workoff_commodity(self):
        name = input('售出商品名称：')
        result = self.checkBook_commodity(name)
        print(result)
        if result != None:
            if result.startus == 0:
                print('商品【%s】已无库存' % name)
            else:
                result.startus = 0
                print('商品 【%s】已售出' % name)
        else:
            print('无商品【%s】库存' % name)
    def supplement_commodity(self):
        name = input('补充商品：')
        result = self.checkBook_commodity(name)
        if result != None:
            if result.startus == 0:
                result.startus = 1
                print('商品【%s】已补充' % name)
                print(result)
        else:
            print('商品【%s】不存在' % name)

c=Commodity()
c.Menu()