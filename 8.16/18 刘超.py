# 0.写函数,返回一个扑克牌列表,里面有52项,每一项是一个元组
# 例如:
# 	[('红心','A'),('草花','A'),...,('方块','K'),('黑桃','K')]
#
# 第一个参数: ['红心','草花','方块','黑桃']
#
# 第二个参数: ['A','2','3','4',...,'K']

# def joker(a,*args):                 #定义函数  *多个不定长参数(元组)
#     cards=[]                        #创建返回值列表
#     for i in args:                  #遍历不定长参数每一个值
#         for j in a:
#             card=(j,i)              #定义元组中的俩个元素ij的值
#             cards.append(card)      #把每一项元组添加进列表
#     print(cards)
# joker(['红心','草花','方块','黑桃'],'A','2','3','4','5','6','7','8','9','10','J','Q','K')

# 1.编写一个函数cacluate, 可以接收任意多个数,返回的是一个元组.
# 元组的第一个值为所有参数的平均值, 第二个值是大于平均值的所有数

# def cacluate(*args):       #定义函数*args不定长参数是一个元组
#     avg=sum(args)/len(args)          #求出平均值
#     dayu=[]                         #创建大于平均值的空列表存储数据
#     for i in args:
#         if i >avg:                       #遍历找出大于平均值的数并且添加进空列表
#             dayu.append(i)
#     return (avg,dayu)
# print(cacluate(1,2,3,4,5,6,7,8))


# 2.编写一个函数, 接收字符串参数, 返回一个元组,‘ehllo WROLD’元组的第一个值为大写字母的个数, 第二个值为小写字母个数

# def zfc(a):
#     count_upper = 0           #大写的次数
#     count_lower = 0           #小写的次数
#     for i in a:
#         if i.isupper() == True:         #遍历字符串每一项如果是大写就加一次
#             count_upper += 1
#         elif i.islower() == True:           #遍历字符串每一项如果是小写就加一次
#             count_lower += 1
#     return (count_upper, count_lower)
# print(zfc('asdwASDSAD'))

# 3.编写函数, 接收一个列表(包含30个1~100之间的随机整形数)和一
# 个整形数k, 返回一个新列表.
# 函数需求:
# - 将列表下标k之前对应(不包含k)的元素逆序;
# - 将下标k及之后的元素逆序;
# [1,2,3,4,5] 2 [2,1,5,4,3]
# import random
# def paixu(a,k):
#     list1=a[:k]          #list1下标K之前的元素
#     list2=a[k:]          #list2下标K之后的元素
#     list1.reverse()            #反转下标K之前和K之后的元素
#     list2.reverse()
#     new_list=[]                 #新建列表并添加list1和list2
#     new_list.extend(list1)
#     new_list.extend(list2)
#     return new_list
# list=[random.randint(1,101) for i in range(30)]      #列表随机取30个1~100之间的随机整形数
# print(list)
# print(paixu(list,5))

# 4.腾讯笔试题:
# 题目需求:
# 	f(n): 返回n里面的每一位数字的平方和
#     对于一个十进制的正整数， 定义f(n)为其各位数字的平方和，如:
#     f(13) = 1**2 + 3**2 = 10
#     f(207) = 2**2 + 0**2 + 7**2 = 53
#     下面给出三个正整数k，a, b,你需要计算有多少个正整数n满足a<=n<=b,
#     且k*f(n)=n
# 输入:
#     第一行包含3个正整数k，a, b, k>=1,  a,b<=10**18, a<=b;
# 输出：
#     输出对应的答案;
#
# 范例:
#     输入: 51 5000 10000
#     输出: 3 (这些数字n具体是哪些)

def f(n):     #定义函数为其各位数字的平方和
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i) ** 2
    return sum
try:
    while True:
        k, a, b = map(int, input('请分别输入三个正整数k,a,b(数字之间用空格隔开即可):').split())
        if k < 1:        #判断范围输入不对有提示  输入数字用空格隔开
            print('k的值不能小于1,请重新输入')
            continue
        if a > 10 ** 18 or b > 10 ** 18:
            print('a和b的值都需要小于10的18次方,请重新输入')
            continue
        if a > b:
            print('a的值不能大于b,请重新输入')
            continue
        break
    count = 0
    print('满足条件的正整数n是:')
    for n in range(a, b + 1):      #判断有多少个正整数n满足a<=n<=b,b取不到要b+1
        if k * f(n) == n:
            print(n, end=' ')
            count += 1
    print()
    print('共%s个正整数' % (count))
except:
    print('输入数字的时候,写完每个数打空格回车不要回车')
