def get_greatest_common(a:int,b:int):   #暴力法
    big = max(a,b)
    small = min(a,b)
    if big % small == 0:
        return small
    for i in range(small // 2,1,-1):
        if big % i == 0 and small % i == 0:
            return i


def get_greatest_common2(a:int,b:int):  #递归实现，辗转相除法，(欧几里得算法)
    big = max(a,b)
    small = min(a,b)
    if big % small == 0:
        return small
    return get_greatest_common(small,big % small)
# print(get_greatest_common(88,24))

def get_greatest_common3(a:int,b:int):     #相减法
    if a-b ==0:
        return a
    big = max(a,b)
    small = min(a,b)
    return get_greatest_common3(small,big - small)
print(get_greatest_common2(88,24))