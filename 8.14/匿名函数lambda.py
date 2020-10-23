# 字符串的比较: 从左往右进行比较,一位一位比,如果有个数值要大,那么该数据就是大的
#
# sorted使用场景: 列表里面是一个个字典的时候进行排序
#
# filter(function,列表): 从列表中筛选数据
#
# 筛选条件在function的返回值里面
#
# 匿名函数: 实现简单的功能
#
# 格式: lambda 形参:返回值
#
# 结合if..else使用
# 
# 格式: lambda 形参:条件成立的返回值 if 条件 else 条件不成的时候的返回值

# 练习:

a = [
    {'name': 'aa','age': 80},
    {'name': 'zs1','age': 30},
    {'name': 'aasd32','age': 50},
    {'name': 'zs12','age': 10},
    {'name': 'zsaqew','age': 20},
    {'name': 'zs213','age': 100},
    {'name': 'zswer','age': 3}
]
# 1.使用def的函数的方式,取出大于20的数据,并且从小到大排序
#
# 2.使用匿名函数的方式,取出名字带有字母a的数据,并且从小到大排序


def f(n):
     #n代表每一个列表中的元素
     return n['age'] >= 50
def f1(n):     #n代表列表中的每一个元素
    print(n)
    return n['age']    #按照年龄进行排序=

result = list(filter(f, a))
print(result)
result =sorted(result,key=f1)
print(result)
# result=sorted(a,key=f)
# print(result)

#取出带有字母a的数据


print(list(filter(lambda n:'a'in n['name'],a)))
result=sorted(result,key=(lambda n:n['age']))
print(result)
