from randomList import randomList
from typing import List
def selectSort(List):
    size =len(List)
    if size <=1:
        return List
    for i in range(len(List)-1):      #外层循环控制第几轮
        for j in range(i + 1,len(List)):      #内存循环负责找最小值
            if List[i] > List[j]:
                List[i],List[j] = List[j],List[i]
        print('第{}轮排序结果'.format(i))
        print(List)
    return List

if __name__ == '__main__':
    randomList.randomList(10)
    print(selectSort(randomList.randomList(10)))