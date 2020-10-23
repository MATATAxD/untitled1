# a=[1,123,33,4,323,555]
# result=sorted(a,reverse=True)
# print(a)
# print(result)

a=[
    {'name':'zs','age':12},
    {'name':'sds','age':23},
    {'name':'ds','age':25},
    {'name':'sdhah','age':50}




]
#按照年龄进行排序
#选择排序
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]['age']>a[j]['age']:
#             a[i],a[j]=a[j][i]
#
# print(a)
def f(n):     #n代表列表中的每一个元素
    print(n)
    return n['age']    #按照年龄进行排序



result=sorted(a,key=f)
print(result)



# a='101'  #字符串比较 从左往右比较一位一位的比较如果有一个数值较大那就是最大的
# b='20'
# print(a>b)
# a='哈哈'
# b='呵呵'
# print(a>b)