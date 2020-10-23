# 1.调用列表操作的常用函数实现以下功能:
#- 1)创建一个空列表score
score=[]
# - 2)在score列表中依次追加10个数值([68, 87, 92, 100, 76, 88, 54, 89, 76, 61] )
score.extend([68, 87, 92, 100, 76, 88, 54, 89, 76, 61])
# print(score)
# - 3)输出score列表中第3个元素的数值
# print(score[2])
# 4)输出score列表中第1～6个元素的值
# print(score[0:6])  #方法1用切片
# for i in range(0,6):            #方法2用for循环遍历列表
#     print(score[i],end=' ')
# print()
# - 5)在score列表第3个元素之前添加数值59
score.insert(2,59)
# print(score)
# - 6)利用变量num保存数值76，查询76分在score列表中出现的次数
# a=score.count(76)
# print(a)
# - 7)查询列表中是否有num76分的考试成绩
# num=76
# if num in score == True:
#     print('是')
# else:
#     print('否')
# - 8)查询score列表中成绩是满分的学生学号
# a=score.index(100)+1
# print(a)
# - 9)score列表中将59分加1分
# score[score.index(59)]+=1
# print(score)
# - 10)删除score列表中第1个元素
# score.pop(0)
# print(score)
# - 11)获得score列表中元素的个数
# count=0
# for i in score:
#     count+=1
# print(count)
# - 12)对列表中所有元素进行排序，输出考试的最高分和最低
# score.sort(reverse=True)   #从大到小排序
# print(score)
# print('考试最高分%s''考试最低分%s'%(score[0],score[len(score)-1]))
# - 13)颠倒score列表中元素的顺序
# score.sort(reverse=True)
# print(score)
# - 14)删除score列表中尾部的元素
# score.pop()
# - 15)score列表中追加数值88，并输出。删除score列表中第一个数值88
# score.append(88)
# print(score)
# score.remove(88)
# print(score)
# - 16)创建2个列表score1和score2,score1中包含数值2个元素值80,61,score2中包含3个元素值71,95,82，合并这两个列表，并输出全部元素
# score1=[80,61]
# score2=[71,95,82]
# score1=score1+score2
# print(score1)
# - 17)创建score1列表，其中包含数值2个元素值80,61，将score1中元素复制5遍保存在score2列表中，输出score2列表中全部元素。
# score1=[80,61]
# score2=score1*5
# print(score2)
# 2.[68, 87, 92, 100, 76, 88, 54, 89, 76, 61] 去除列表中的偶数  --> [87,89,61]
# a=[68, 87, 92, 100, 76, 88, 54, 89, 76, 61]
# b=[]  #创建空列表存储元素
# for i in a:   # for循环遍历列表每个元素
#     #print(i,end=' ')
#     if i % 2 !=0:   #判断每个元素是否为偶数
#         b.append(i)   #如果没有就填加到新列表
#         # print(b)
# a=b.copy()  #重新赋值列表就是去除偶数的列表
# print(a)
# 3.双色球: 红色球可以在1-33个编号中任意选择6个，蓝色球可以在1-16中选择一个
# 要求: 随机生成双色球,使用列表输出,前6个红球,最后1个是篮球 (去重,random)
# import random
# a=[] #建一个新列表用来去重不会有重复值
# while True:
#     b=random.randint(1,33)  #建一个b列表取1-33随机数
#     if b not in a:
#         a.append(b)      #当b中的随机数不再列表a中就放之前的列表a中
#     if len(a)==6:        #当列表元素够6个时候终止循环
#         break
# # print(a)
# a.append(random.randint(1,16))   # 在列表末尾添加蓝色球
# print(a)
# 4.请写出一段 Python 代码实现分组一个 list 里面的元素, [1,2,3,...100]变成 [[1,2,3], [4,5,6]....,[97,98,99],[100]]
# a=[]
# for i in range(1,101):   #创建一个1-100的列表
#     a.append(i)
#     # print(a)
# b=[]     #创建新列表存储新的元素
# for j in range(0,len(a),3):
#     c=a[j:j+3]     #用切片切割列表的元素
#     b.append(c)      # 把切片的元素放入新列表
# print(b)

#5. 用户输入n,生成含有 n 个元素值为 1~n 的列表,元素顺序随机,但值不重复:
# 	8  [1,2,3,4,5,8,6,7]
# 	3  [1,3,2]
# import random
# n=int(input('输入一个整数'))
# a=[]                    #新建列表存储元素
# for i in range(1,n+1):  #遍历输入整数的列表每一个元素
#     a.append(i)         # 把遍历的元素添加到a列表
# b=random.sample(a,n)    #列表里面随机取N个数值
# print(b)
# 6.自己实现列表的sort方法 (排序算法)
#   [12,3123,123,3,4,354,3] --> [3,3,4,12..]
# a=[12,3123,123,3,4,354,3]
# a.sort()       #方法一用sort方法排序
# print(a)
#方法二 用冒泡排序
# for i in range(len(a)-1):   #控制总共的循环次数
#     for j in range(len(a) - 1 - i):  #控制相邻俩个数的比较，每次外层循环之后最后一个数不用比较，因为最后一个数就是最大值
#         if a[j] > a[j+1]:           #j当前位置的下标,j+1下一个位置的下表，当第一个数比第二个数大时候就交换位置
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)

# 7.写一个循环，不断的问用户想买什么，用户选择一个商品编号(下标)，就把对应的商品添加到购物车(列表)里，最终用户输入q退出时，打印购物车里的商品列表. 数据
# products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],['wife',10],['wifi',100000]]
#
# 结果: 输出买的所有商品名字,格式为:
# 	你购买的商品为: iphone8: 个数(count)	MacPro:个数...
# 	总价为: xx元
#
#
# 价格和商品名字一一对应
# products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],['wife',10],['wifi',100000]]
# sum=0
# price_name_list=[]   #创建商品价格列表
# while True:
#     shuru=input('输入购买的商品序号:')
#     try:    #用户输入验证
#         if shuru == 'q':
#             print('退出程序')
#             break
#         elif int(shuru) in range(0,len(products)):
#             index=int(shuru)                      #输入的商品下标值序号
#             price=products[index][1]              #取出每个商品的价格
#             sum += price                          #价格求和
#             price_name=products[index][0]         #取出每个商品的名称    price_name 商品价格
#             price_name_list.append(price_name)    #加入商品价格列表
#
#         else:
#             print('输入正确序号')
#     except Exception as e:
#         print('输入正确数字')
# print('总价为:%s'%(sum))                          #求出商品的总价
# #print(price_name_list)
#
# new_name_list=[]                                        #新建列表商品的名称用来去重
# print('你购买的商品为:',end='\t')
# for name in price_name_list:                            #name去重后的商品名字 price_name_list.count商品名字记数
#     if name not in new_name_list:
#         price_count=price_name_list.count(name)          # price_count 计算用户选中的商品次数  计算商品次数去重
#         new_name_list.append(name)                        #把去重后的商品次数加入new_name_list列表
#         print('%s:%s'%(name,price_count),end='\t')          #求出商品的名字和次数



