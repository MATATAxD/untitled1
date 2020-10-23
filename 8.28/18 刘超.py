# 1.实现一个单类
#工人类
# class Worker:
#     def __init__(self,name,sex,age,height,salary):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.height = height
#         self.salary = salary
#     def eat(self):
#         print('%s在吃饭...'%(self.name))
#     def sleep(self):
#         print('%s在睡觉...'%(self.name))
#     def work(self):
#         print('%s在上班'%(self.name))

# 2实现冒泡选择排序
# 冒泡排序
# a=[55,20,10,9,5]
# for i in range(len(a)-1):
#     for j in range(len(a)-1-i):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
# # 选择排序
# for i in range(len(a)):
#     for j in range(i + 1,len(a)):
#         if a[i] > a[j]:
#             a[i],a[j] = a[j],a[i]
# print(a)

# 3输出1-100间的所有质数
# for i in range(2,101):
#     j=2
#     while i%j != 0:
#         j=j+1
#     if j==i:
#         print (i,end=' ')

#4逗号隔开输入某年某月某日，判断这一天是这一年的第几天？
#平年的月份天数平年2月28天
# p_list = [0,31,59,90,120,151,181,212,243,273,304,334]
# #闰年的月份天数闰年2月29天
# r_list = [0,31,60,91,121,152,182,213,244,274,305,335]
# str1 = input('请输入年月日:')
# a, b, c = str1.split('.')
# #年月日a,b,c
# a = int(a)
# b = int(b)
# c = int(c)
# def f(str1):
#     #判断平年还是闰年
#     if (a % 100 == 0 and a % 400 == 0) or (a % 100 != 0 and a % 4 == 0):
#         return r_list[b-1]+c
#     else:
#         return p_list[b-1]+c
# print(f(str1))

# 5.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# a = [100]  #每个反弹落地过程经过的路程，第1次只有落地（100米）
# h = 100  #每个反弹落地过程，反弹的高度，第1次为100米
# print('第1次从%s米高落地，走过%s米，之后又反弹至%s米。' % (h, a[0], h/2))
# for i in range(2,11):
#     a.append(h)  #先计算路程，再高度减半，因为一个反弹落地为2个高度
#     h = h / 2
#     print('第%s次从%s米高落地，共走过%s米，之后又反弹至%s米。' % (i, h, sum(a), h / 2))

#6. 将字符串"a-b-c-d-e-f"倒叙输出,中间字符变为大写: “f-e-d-C-b-a”
# a="a-b-c-d-e-f"
# index=len(a)//2-1
# #print(index)
# a = a.replace(a[index],chr(ord(a[index]) - 32))
# b=a.split('-')
# b.reverse()
# b='-'.join(b)
# print(b)
# 7.实现函数strip,要求自己实现去除字符串首尾空格的功能
# def trim(s):
#     if s[:1] != ' ' and s[-1:] != ' ':
#         return s
#     elif s[:1] == ' ':
#         return trim(s[1:])
#     else:
#         return trim(s[:-1])
# print(trim('  hello'))
# 8.功能描述：删除字符串中字符个数最少的字符，而且最少字符串有多个，最少的要全部删除 然后返回该字符串
# shuru = input('请输入字符串: ')
# list = []
# count_list = []
# # 遍历字符串
# for i in shuru:
#     # 每个字母出现的次数
#     count = shuru.count(i)
#     if i not in list:
#         list.append(i)
#         count_list.append(count)
# # 用选择排序进行从小到大排序
# for i in range(len(count_list)):
#     for j in range(i + 1,len(count_list)):
#         if int(count_list[i]) > int(count_list[j]):
#             count_list[i],count_list[j] = count_list[j],count_list[i]
# # 在字符串中出现最少字母的次数
# min = count_list[0]
# for i in range(count_list.count(min)):
#     for i in shuru:
#         count = shuru.count(i)
#         if count == min:
#             shuru = shuru.replace(i,'')
# print('输出为:%s'%(shuru))



# 9.随机生成，100个从1到10的随机整数，然后每个偶数出现的次数:
# 例如: 1,2,3,2,3,1,5,6,10,2
# 输出: {“2”: 3,”6”: 1 “10”: 1}
# import random
# a = []
# dic ={}
# for i in range(1,10):
#     a.append(i)
# randomlist = random.choices(a,k=100)
# print(randomlist)
# count = 0
# for i in randomlist:
#     if i % 2 ==0:
#         dic['%s'%i] = randomlist.count(i)
# print(count)
# print(dic)


#10.用户输入日期,判断是否为日期,格式如下: 2018-12-6,年份1-9999,月份01-12或者1-12,天数01-31或者1-31,不用考虑每个月的具体天数,例如: 2018-2-31也满足
# import re
# shuru = input('请输入一个日期:')
# pattern = r'^[0-9]{4}\-(0?[1-9]|[1][012])\-(0?[1-9]|[12][0-9]|[3][01])$'
# result = re.search(pattern,shuru)
# if result == None:
#     print('不是正确日期')
# else:
#     print('是正确日期')
