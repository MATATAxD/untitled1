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
msg = '''==================================================
   双色球 V0.01
 1. 充值  （先显示原有金额，再输入金额，最后显示充值后的金额）
 2. 随机生成一个彩票 (显示生成的彩票: 红球: 12... 蓝球: 蓝球号码)
 3. 手动输入彩票号码(总共输入7个号码,每个号码中间逗号隔开,前六个是红球号码,最后一个是蓝球号码): 1,2,3,4,5,6,7
 4.查看最新一期彩票结果, 显示开奖后的账户余额 （最新一期彩票结果随机产生）
 5. 显示当前余额
 6. 显示所有的彩票:
 7.	退出系统
=================================================='''
print(msg)
balance=10
#所有的彩票
allTickets=[]
# 充值
def addMoney(money):
    global balance
    balance+=money
    print('充值成功')
    print('充值后的金额为:%s'%(balance))
#显示当前余额
def showBalance():
    print('当前余额为:%s'%(balance))
#随机生成一张彩票
def randomTicket():
    # {'red': [6个1-33的数字],'blue': 1-16}
    # random.sample(列表,n) : 从列表里面取出n个不重复的数字
    # 1-33的红球列表
    redList = list(range(1,34))
    # 取出6个数 (红球)
    red = random.sample(redList,6)
    # 蓝球
    blue = random.randint(1,16)
    dic = {'red': red,'blue': blue}
    return dic
# 随机购买一张彩票
def randomBuyTicket():
    global balance
    # 判断余额支不支持购买彩票
    if balance >= 2:
        # 随机生成彩票
        dic = randomTicket()
        # 把生成的彩票放入allTickets里面
        allTickets.append(dic)
        # 购买成功之后,显示用户所买的彩票
        print(dic)
        # 余额递减
        balance -= 2
        # 显示余额
        showBalance()
    else:
        print('余额不足,请及时充值')
#显示一张彩票
def showTicket(dic):
    red=dic['red']
    for i in range(len(red)):            #把红球转化为字符串类型
        red[i]=str(red[i])
    redResult=','.join(red)                  #转化为中间隔开的字符串
    bule=dic['bule']
    print('红球',redResult,'篮球',bule)

#显示所有的彩票
def showAlltickets():        #每张彩票都在alltickets 里面
    for ticket in allTickets:
        showAlltickets(ticket)   #ticket 字典每张彩票
#中奖
def prize():
    zhongjiang=randomTicket()    # 中奖的彩票随机生成
    print('中奖的彩票号码为:')
    showTicket(zhongjiang)
    for me in allTickets:       # 中奖操作(每个彩票都得判断是否中奖,中的是什么奖)
        # me: 每一张彩票
        # 自己买的红球
        red = me['red']
        # 自己买的蓝球
        blue = me['blue']
        # 红球的中奖个数
        redCount = 0
        for i in red:
            if i in zhongjiang['red']:
                redCount += 1
        # 蓝球的中奖个数
        blueCount = 0
        if blue == zhongjiang['blue']:
            blueCount += 1
        print(me,redCount, blueCount)
        # 中奖说明
        if redCount == 6 and blueCount == 1:
            print('中6+1')
            # 把1000万加给余额
            balance += 10000000
        elif redCount == 6 and blueCount == 0:
            print('中6+0')
            balance += 5000000
        elif redCount == 5 and blueCount == 1:
            print('中5+1')
            balance += 3000
        elif redCount == 5 and blueCount == 0:
            print('中5+0')
            balance += 200
        elif redCount == 4 and blueCount == 1:
            print('中4+1')
            balance += 200
        elif redCount == 4 and blueCount == 0:
            print('中4+0')
            balance += 10
        elif redCount == 3 and blueCount == 1:
            print('中3+1')
            balance += 10
        elif redCount == 2 and blueCount == 1:
            print('中2+1')
            balance += 5
        elif redCount == 1 and blueCount == 1:
            print('中1+1')
            balance += 5
        elif redCount == 0 and blueCount == 1:
            print('中0+1')
            balance += 5
        else:
            print('很抱歉,该彩票未中奖')

    # 显示余额
    showBalance()
# zhongjiang：要进行对比的彩票
# me:自己购买的彩票
def ticketCount(zhongjiang,me):
    red=me['red']      #自己购买的红球
    blue=me['blue']         #自己购买的蓝球
    redCount=0                        #红球的中奖个数
    for i in red:
        if i in zhongjiang['red']:
            redCount+=1
    blueCount=0                  #蓝球中奖个数
    if blue ==zhongjiang['blue']:
        blueCount+=1
    return [redCount,blueCount]          #返回和红球相同的数字和蓝球相同的数字

# 手动购买彩票
def inputTicketNum():
    while True:
        userinput=input('输入彩票号码(总共输入7个号码,每个号码中间逗号隔开,前六个是红球号码,最后一个是蓝球号码): ')
        userinput=userinput.replace(' ','')    #如果输入空格换成空字符串
        userinput=userinput.split(',')      #根据逗号分割为列表
        #如果用户输入小于7或者大于7
        if len(userinput)==7:
            for i in range(len(userinput)):
                if userinput[i][0]==[0]:
                    userinput[i]=userinput[i][1:]   #如果第一位是0去掉0
                try:
                    userinput[i]=int(userinput[i])    #将列表中元素转换为数字类型
                except:
                    print('输入内容有误请输入正确的内容不能出现字母或者汉字')
                    break
            # 当循环结束以后,userInput里面就是纯数字类型的列表
            # [1,23,31,020,2,6,1]
            # 红球重复
            # 红球列表
            redList=[]
            flag=False
            for red in redList:
                # red: 每个红球
                if redList.count(red) > 1:   # 判断每个红球出现的次数,如果大于1,则重复
                    flag = True
                    print('红球当中有重复的数字,请重新输入..')
                    break
                if red < 1 or red > 33:       # 判断红球的范围: 1-33
                    flag = True
                    print('红球的数字超出范围,应该在1-33之间,请重新输入')
                    break
            if flag:
                # 当红球有问题,底下的代码不执行了
                continue
            # 蓝球(最后一项)
            blue = userinput[len(userinput) - 1]
            # 蓝球的范围 1 16
            if blue < 1 or blue > 16:
                print('蓝球的数字超出范围,应该在1-16之间,请重新输入')
            else:
                # 蓝球和红球都没有问题
                print('购买成功!!')
                dic = {'red': redList, 'blue': blue}
                # 显示生成的红球和蓝球
                showTicket(dic)
                break




while True:
    userinput=input('输入操作序号')
    if userinput =='1':     #充值
        showBalance()
        money=int(input(('输入充值金额')))
        addMoney(money)
    elif userinput =='2':     #随机购买一张彩票
        randomBuyTicket()
    elif userinput =='3':       #手动输入彩票号码
        pass
    elif userinput =='4':
        prize()                   #中奖
    elif userinput =='5':          #显示当前余额
        showBalance()
    elif userinput =='6':          #显示所有的彩票
        allTickets()
    elif userinput =='7':
        print('退出系统')
        break
    else:
        print('输入正确的序号')






