from typing import List
def hanmingjuli(x:int,y:int):
    a=x^y
    count=0
    while a!=0:
        a=a&(a-1)
        count+=1
    return count
if __name__ =="__main__":
    print(hanmingjuli(4,14))
    # 用异或能把相同位置转为0 不同位置为1  找不同不位置数目 不同位置就成了1