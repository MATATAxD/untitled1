from typing import List
from randomList import randomList


def insertSort(List):
    if len(List) <= 1:
        return List
    for right in range(1, len(List)):
        targrt = List[right]
        for left in range(0, right):
            if List[left] > targrt:
                List[left + 1:right + 1] = List[left: right]
                List[left] = targrt
                break
        print('第{}轮排序结果'.format(right))
        print(List)
    return List

if __name__ == '__main__':
    randomList.randomList(10)
    print(insertSort(randomList.randomList(10)))

