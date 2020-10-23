# # 0.实现简易计算器功能,如图
# a = int(input('输入第一个数'))
# b = int(input('输入第二个数'))
# c = input('输入要做的运算:(+,-,*,/)')
# if c == '':  # 如果输入为空默认为加法运算
#     result = a + b  # 运算结果
#     print(result)
# elif c == '+':     #如果输入为+就是加法运算
#     result = a - b
#     print(result)
# elif c == '-':      #如果输入为-就是减法运算
#     result = a - b
#     print(result)
# elif c == '*':        #如果输入为*就是乘法运算
#     result = a * b
#     print(result)
# else:                  #如果输入为/就是除法运算
#     c == '/'
#     result = a /b
#     print(result)


# 1.让用户输入两个任意的整数, 比较两个数的大小, 输出最大的数
# a=int(input('输入第一个数'))
# b=int(input('输入第二个数'))
# if a > b:
#     print(a)
# else:
#     print(b)

# 2.用户输入一个数,打印出奇数还是偶数
# a=int(input('输入一个数'))
# if a%2==0:   #判断是否偶数
#     print('偶数')
# else:        #判断是否奇数
#     print('奇数')

# 3.用户输入帐号密码,帐号为admin,密码为8888显示登录成功,其余的显示登录失败
# user=input('输入账号')
# password=input('输入密码')
# if user=='admin' and password=='8888':
#     print('登录成功')
# else:
#     print('登录失败')

# 4.用户输入一个三位数,输出结果是否为水仙花数(水仙花数: 水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。)
# a=int(input('输入一个三位数'))
# b=a//100 #百位数
# c=a//10%10    #十位数
# d=a%10        # 个位数
# if b**3+c**3+d**3==a:  #判断是否水仙花算法
#     print('是水仙花数')
# else:
#     print('不是水仙花数')

# 5.用户输入年份,输出结果是闰年还是平年(闰年: 1.能整除4且不能整除100 2.能整除400)
# years = int(input('输入年份'))
# if years % 4 == 0 and years // 100 != 0 or years % 400 == 0:  #判断是否闰年
#     print('闰年')
# else:
#     print('平年')

# 6.输入公交卡当前的余额,空座位数，只要超过2元，就可以上公交车;没钱,撵走；如果空座位的数量大于0，就可以坐下;
# money = int(input('输入余额'))
# zuowei = int(input('空座位数'))
# if money >= 2:
#     print('上车')
#     if zuowei > 0:
#         print('坐下')
#     else:
#         print('无座')
# else:
#     ('撵走')

# 7.成绩等级:
# 	90分以上:  等级为A
#
# 	80-90: 等级为B
#
# 	60-70: 等级C
#
# 	0-60: 等级为D
# chenji=int(input('输入成绩'))
# if chenji >=90:
#     print('等级A')
# elif chenji >=80 and chenji <90:
#     print('等级B')
# elif chenji >=60 and chenji<70:
#     print('等级C')
# else:
#      chenji >=0 and chenji<60
#      print('等级D')

# 8.场景应用: 上火车 (用户输入表示是否有票,是否有刀具)
# 	是否有票,有票打印可以进站;
# 	进站查看是否带有刀具,有刀具,没收上车,没有刀具,直接上车
# 	没票打印不可以进站
# a = input('输入是否有票')
# if a == '是':
#     print('打印可以进站')
#     b = input('是否有刀具')
#     if b == '是':
#         print('没收上车')
#     else:
#         print('直接上车')
# else:
#     print('不可进入')

# 9.女友的节日:
# 	定义holiday_name字符串变量记录节日名称
# 	如果是 情人节 应该 买玫瑰／看电影
# 	如果是 平安夜 应该 买苹果／吃大餐
# 	如果是 生日 应该 买蛋糕
# 	其他的时候,每天都是节日
# holiday_name =input('输入今天是什么叫节日')
# if holiday_name == '情人节':
#     print('买玫瑰/看电影')
# elif holiday_name == '平安夜':
#     print('买苹果/吃大餐')
# elif holiday_name == '生日':
#     print('买蛋糕')
# else:
#     holiday_name=='其他时候'
#     print('每天都是节日')

# 10.英雄联盟(LOL)李青技能:
# q,Q:天音波
# w,W:金钟罩/铁布衫
# e,E:天雷破/摧筋断骨
# r,R:猛龙摆尾
# a = input('输入技能')
# if a == 'q' or a == 'Q':
#     print('天音波')
# if a == 'w' or a == 'W':
#     print('金钟罩/铁布衫')
# if a == 'e 'or a == 'E':
#     print('天雷破/摧筋断骨')
# if a == 'r' or a == 'R':
#     print('猛龙摆尾')


# 11.用户决定是否发工资,工资数是多少,信用卡欠款;有剩余的时候,显示剩余金额(图1)
# a = input('输入是否发工资')
# if a == 'yes':
#     print('先还信用卡的钱')
#     b = input('是否还有剩余')
#     if b == 'yes':
#         print('又可以happy了')
#     elif b == 'no':
#         print('噢NO')
# else:
#     print('盼工资')


# 12.让用户输入三个任意的整数, 比较三个数的大小, 输出最大的数
# a = int(input('输入第一个整数'))
# b = int(input('输入第二个整数'))
# c = int(input('输入第三个整数'))
# if a > b and a > c:   #判断a和b a和c的大小 如果A最大
#     print(a)
# elif a < b and b > c:    #判断 a和b b和c的大小 如果 b最大
#     print(b)
# else:
#     print(c)
