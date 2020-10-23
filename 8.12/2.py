# 练习:
# 1. [12,12,234,32,32,234] [13,14,123,13,14,234] [1,1,1,1,324,23,4,32,2,2] (实现列表去重操作)
# 结果: 直接运行,就打印出三个列表去重后的效果
# a=[12,12,234,32,32,234]
# b=[13,14,123,13,14,234]
# c=[1,1,1,1,324,23,4,32,2,2]
# def quchong(list):
#     new_list=[]
#     for i in list:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
# print(quchong(a))
# print(quchong(b))
# print(quchong(c))

# 2. [12,12,234,32,32,234] [13,14,123,13,14,234] [1,1,1,1,324,23,4,32,2,2]
#
# 结果: 直接运行,就打印出三个列表排序后的效果
# a=[12,12,234,32,32,234]
# b=[13,14,123,13,14,234]
# c=[1,1,1,1,324,23,4,32,2,2]
# def paixu(list):       #冒泡排序
#     for i in range(len(list) - 1):
#         for j in range(len(list) - 1 - i):
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
#     return list
# def paixu1(list):       #选择排序
#     for i in range(len(list)):
#         for j in range(i + 1, len(list)):
#             if list[i] > list[j]:
#                 list[i], list[j] = list[j], list[i]
#     return list
# print(paixu(a))
# print(paixu(b))
# print(paixu(c))
# print(paixu1(a))
# print(paixu1(b))
# print(paixu1(c))





# 3. 求1-100,500-1000,3000-5000的和

# def sum(start,stop):    # start要求数字 起始值  stop要求数值末位值
#     sum=0
#     count=1
#     for i in range(start,stop+1):
#         sum+=count
#         count+=1
#     return sum
# print(sum(1,100))
# print(sum(500,1000))
# print(sum(3000,5000))










