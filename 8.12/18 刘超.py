# 0.写函数,传入一个参数n,返回n的阶乘的结果
# 例如: cal(5)  返回的结果为: 5 * 4 * 3 *  2 * 1
# def jiechen(n):
#     if n <0:    #如果n小于0结束
#         exit()
#     sum = 1
#     for i in range(1,n+1):   #算出阶乘
#         sum* = i
#     return sum
# print(jiechen(5))

# 1.写函数,要求传入列表或者元组,取得下标为偶数的值作为新的列表或者元组,返回给调用者
# def oushu(a):
#     b=[]       #建空列表存放数据
#     for i in range(0,len(a),2):   #遍历 找出下标为偶数的值
#         b.append(a[i])
#     return b
# a = [1,2,3,4,5,6,7,8,9,10]   #测试
# print(oushu(a))

# 3.写函数,检查列表的长度,如果大于5,则将列表的前5项内容返回给调用者
# def jiancha(a):
#     if len(a)>5:        #判断列表长度是否大于5
#         b = a[0:5]        #判断如果是用切片返回前五项
#     return b
# a = [1,2,3,4,5,6,7,8,9,10]    #测试
# print(jiancha(a))

# 4.写函数,要求传入一个字符串,统计每个字符出现的次数,将其制作为字典返回给调用者
# def tongji(a):
#     b={}     #创建字典存放结果
#     for i in a:            #统计字符串出现次数添加到字典
#         b[i] = a.count(i)
#     return b
# a='wekwqekj'              #测试
# print(tongji(a))

# 5.写函数,接收三个参数,返回值较大的那个数字
# def max(a,b,c):
#     Max=a         #假设最大值为max也就是a
#     if b>Max:         #如果b大于max最大值为b
#         Max = b
#     if c>Max:         #如果c大于max最大值为c
#         Max = c
#     return Max
# print(max(5,6,7))         #测试


# 6.写函数,检查传入字典的每一个value的长度,如果大于2,那么仅保留前两个长度的内容,并组合为新字典返回给调用者
# 例如:
# 传入:
# 	dic = {'k1': 'v1v2','k2': [11,22,33,44]}
# 返回:
# 	dic {'k1': 'v1','k2': [11,22]}
#
# 假定value只能是列表或者字符串
# def jiancha(a):
#     for i in a:
#         if len(a[i])>2:                #遍历找出value长度如果大于2取前俩个长度重新赋值
#             a[i]=a[i][0:2]
#     return a
# a={'k1':'v1v2','k2':[11,22,33,44]}           #测试
# print(jiancha(a))



# 双色球彩票系统: 6个功能全部封装成函数.
#
# # 自己的余额自己设置
# price = 10000
#
# [{'red': 红球列表,'blue': 蓝球},{'red': 红球列表,'blue': 蓝球}]
#
# 彩票: {
# 	'red': [],
# 	'blue': int
# }
#
# 一张彩票:
# {'red': [],'blue': int}
#
# 所有的彩票:[{'red': [],'blue': int},{'red': [],'blue': int},{'red': [],'blue': int},{'red': [],'blue': int},{'red': [],'blue': int}]
#
#
# - 从1-33共33个红色号码球中选择6个号码，并从1-16共16个蓝色号码球中选择1个号码
#
#
# - 交互大框架 （原始金额自定，彩票2元一张）
# ==================================================
#    双色球 V0.01
#  1. 充值  （先显示原有金额，再输入金额，最后显示充值后的金额）
#  2. 随机生成一个彩票 (显示生成的彩票: 红球: 12... 蓝球: 蓝球号码)
#  3. 手动输入彩票号码(总共输入7个号码,每个号码中间逗号隔开,前六个是红球号码,最后一个是蓝球号码): 1,2,3,4,5,6,7
#  4.查看最新一期彩票结果, 显示开奖后的账户余额 （最新一期彩票结果随机产生）
#  	格式:
#  	本期彩票的结果为: 红球: 1,2,3,4,5,6 蓝球: 1
#  	中6+1 奖金1000万
#  	中5+0 奖金200
#  	...
#  	...
#  	...
#  	最终账户余额为: xxxx
#  5. 显示当前余额
#  6. 显示所有的彩票:
#  			红球: 6个数字  蓝球: 1
#  			红球: 6个数字  蓝球: 1
#  			红球: 6个数字  蓝球: 1
#  			红球: 6个数字  蓝球: 1
#  			红球: 6个数字  蓝球: 1
#  7.	退出系统
# ==================================================
#     请输入操作序号:

import random
def chongzhi():   #充值操作
    global money
    print('您原有金额为:',money)
    a=int(input('输入要充值的金额:'))
    money+=a
    print('充值后的金额:',money)

def yue():
    global money
    print('当前余额为:',money)

def xianshi(a):
    print("红球:", end=" ")
    for i in range(0, 6):
        if i == 5:
            print(a["red"][i], end="\t")
        else:
            print(a["red"][i], end=",")
    print("蓝球:", a["blue"])

def shengcheng():
    a={}
    b=list(range(1,34))
    red=random.sample(b,6)
    a['red']=red
    a['blue']=random.randint(1,17)
    global cards
    global money
    cards.append(a)
    money-=2
    xianshi(a)

def shoudong():
    a = input("请输入彩票号码:")
    b = a.split(",")
    c = {"red": []}
    for i in range(0, len(b)):
        if i == len(b) - 1:
            c["blue"] = int(b[i])
        elif i in range(0, len(b) - 1):
            c["red"].append(int(b[i]))
    global cards
    global money
    cards.append(c)
    money -= 2
    xianshi(c)

def suoyou():
    global cards
    for i in cards:
        xianshi(i)




def menu():
    print('''
==================================================
                双色球 V0.01
    1. 充值
    2. 随机生成一个彩票
    3. 手动输入彩票号码
    4.查看最新一期彩票结果, 显示开奖后的账户余额
    5. 显示当前余额
    6. 显示所有的彩票
    7.	退出系统
==================================================
''')
money=10000
cards=[]
while True:
    try:
        menu()
        shuru = int(input('输入操作序号:'))
        if shuru ==7:
            print('退出系统')
            break
        elif shuru ==1:
            chongzhi()
        elif shuru ==2:
            shengcheng()
        elif shuru ==3:
            shoudong()
        elif shuru ==4:
            pass
        elif shuru ==5:
            pass
        elif shuru ==6:
            suoyou()
        else:
            print('请输入正确的序号!')
    except Exception as e:
        print('请输入正确的数字序号!',e)




