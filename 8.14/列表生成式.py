# a=list(range(101))     #生成1-100
# a=a[1:]
# print(a)

# a=[i for i in range(1,101)]
# print(a)



#1-100列表用字符串表示
a=[str(i) for i in range(1,101)]
print(a)
# a=[10,123,23,423,423]
# # for i in range(len(a)):
# #     a[i]+=1
# # print(a)
a=[1,2,3,4,5,6,7]
a=[i+1 for i in a]
print(a)
a=[i **2 for i in a]
print(a)
