import time
start =time.time()
def fib(n):  #斐波纳契数列 :1,1,2,3,5,8,13,21...也就是每个数等于它前俩个数之和。那么给你第N个数，问F(n)是多少
    if n <=2:
        return 1
    return fib(n-1) + fib(n-2)
# start = time.time()
# print(fib(40))
# end =time.time()
# dur = end - start
# print(dur)

# 求阶乘
def fib1(n):
    if n<=2:
        return n
    return  fib1(n-1)*n
print(fib1(4))#

def fib2(n):
    if n<=2:
        return n
    return fib(n-1)+fib(n-2)
print(fib2(4))
