# 3.双色球: 红色球可以在1-33个编号中任意选择6个，蓝色球可以在1-16中选择一个
# import random
# a=[]
# for i in range(1,34):
#     a.append(i)
# b=random.sample(a,6)
# b.append(random.randint(1,16))
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
a=[]
for i in range(1,101):
    a.append(i)
b=[]
for j in range(0,len(a),3):
    c=a[j:j+3]
    #print(c)
    b.append(c)
print(b)

