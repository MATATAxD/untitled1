# 1.Employee 类
# # 	- 员工数 初始值为0, 每当新声明一个实例时,员工数加一
# # 	- 员工: 姓名, 工资
# # 	- 声明方法 displayCount: 打印出当前的总员工数 (类方法)
# # 	- displaySalary : 打印每一个员工自己的名字和薪水.
# class Employee:
#     num=0
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary   #salary工资
#         Employee.num+=1
#     def displaySalary(self):
#         print('姓名:%s,工资:%s'%(self.name,self.salary))
#     @classmethod
#     def displayCount(cls):
#         print('当前员工总数:%s'%(cls.num))
# a=Employee(name='张三',salary=10000)
# a.displayCount()
# a.displaySalary()

# 2.设计一个人的类,有名字,体重;能吃,能跑;
# 	a.每次跑步会减肥0.5公斤
# 	b.每次吃东西体重会增加1公斤
# 	c.有个get_msg()方法,打印出名字,体重:
# 		我的名字叫: xxx 体重是:
# class Person:
#     def __init__(self,name,weight,):
#         self.name=name
#         self.weight=weight
#     def eat(self):
#         self.weight+=1
#     def run(self):
#         self.weight-=0.5
#     def get_msg(self):
#         print('我的名字叫:%s,体重是%s'%(self.name,self.weight))
# a=Person(name='张三',weight=100)
# a.run()
# a.eat()
# a.get_msg()

# 3.定义一个圆类,有半径属性,其中有计算周长和面积的方法
# class Circular:
#     pai = 3.14
#     def __init__(self,banjing):
#         self.banjing=banjing
#     def zhouchang(self):
#         return 2 * Circular.pai * self.banjing   #圆的周长计算公式
#     def mianji(self):
#         return Circular.pai * (self.banjing **2)
# a=Circular(6)
# print(a.zhouchang())
# print(a.mianji())


# 4.补充代码实现:
# 	user_list = []
# 	while True:
# 		user_name = input('输入用户名: ')
# 		sex = input('输入性别: ')
# 		age = input('输入年龄: ')
# 		email = input('输入邮箱: ')
# 	a.把每个用户用对象表示
# 	b.当列表中添加3个对象以后,打印出3个对象的信息:
# 		我叫xxx,性别xx,今年xx岁了,我的邮箱是xxxx
class Person:
    def __init__(self,username,sex,age,email):
        self.username=username
        self.sex=sex
        self.age=age
        self.email=email
    def xianshi(self):
        print('我叫:%s,性别:%s,今年:%s岁了,我的邮箱是%s,'%(self.username,self.sex,self.age,self.email))
user_list = []
count=0
while True:
    user_name = input('输入用户名: ')
    sex = input('输入性别: ')
    age = input('输入年龄: ')
    email = input('输入邮箱: ')
    a=Person(user_name,sex,age,email)
    user_list.append(a)
    count+=1
    if count==3:
        for i in user_list:
            i.xianshi()
        break



