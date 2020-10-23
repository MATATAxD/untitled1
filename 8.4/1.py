#加法计算器
# a=int(input('输入第一个数'))
# b=input('输入第二个数')
# c=int(a)+int(b)
# print(int(c))

#输入一个三位数打印打印三位数的立方和
a=int(input('输入一个三位数'))
b=a//100
c=a//10%10
d=a%10
f=(b**3+c**3+d**3)
print(f)

