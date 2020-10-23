# class Student:
#     def __init__(self,name,sex,age,height,chengji):
#         self.name=name
#         self.sex=sex
#         self.age=age
#         self.height=height
#         self.chengji=chengji
#     def eat(self):
#         print('%s正在吃饭'%(self.name))
#     def sleep(self):
#         print('%s正在睡觉'%(self.name))
#     def kaoshi(self):
#         print('%s正在考试'%(self.name))
#
# p=Student('张三','男',18,180,100)
# p1=Student('李四','男',19,185,80)
# # print(p.name,p.sex,p.age,p.height,p.chengji)
# p.eat()
# p.sleep()
# p.kaoshi()


class gongren:
    def __init__(self, name, sex, age, height, xingzi):
        self.name=name
        self.sex=sex
        self.age=age
        self.height=height
        self.xingzi=xingzi
    def eat(self):
        print('%s正在吃饭'%(self.name))
    def sleep(self):
        print('%s正在睡觉'%(self.name))
    def shangban(self):
        print('%s正在上班'%(self.name))
p=gongren('张三','男',18,180,100)
p1=gongren('李四','男',19,185,80)
p.eat()
p.sleep()
p.shangban()






