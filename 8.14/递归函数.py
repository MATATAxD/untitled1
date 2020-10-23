# 递归函数的思想：把规模大的问题拆分成规模小的问题，然后把规模小的问题再拆分成规模更小的问题...一层层的拆分拆分到一定的程度
# 变成很小的问题，最后问题就解决了
import sys

# count=0
# def f(count):
#     count+=1
#     print(count)
#
#     if count==10:
#         return count
#
#
#     f(count)
# f(count)


# return n + f(n-1)
# # 1-100的和                                 #f(100) return 100+ f(99)
# def f(n):                                   #f(99)  retuun 99 + f(98)
#     return n+f(n-1)                         #f(98)  return 98 + f(97)
#        if n==1:                                     #...
#            return                           #f(2)   return 2+1
# f(100)                                      #f(1)   return 1
#

# def f(n):              #1-100的和
#     if n==1:
#         return 1
#     return n+f(n-1)
# print(f(100))
# def f(n):
#     if n==1:
#         return 1
#     return n*f(n-1)
# print(f(5))
# def f(n):      #斐波那契数列
#     if n==1 or n==2:
#         return 1
#     return f(n-1)+f(n-2)
# print(f(7))

def f(n):
    if n==7:
        return 1
    return (f(n+1)+1)*2
print(f(1))