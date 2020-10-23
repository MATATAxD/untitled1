from randomList import randomList
from typing import List
def bubbleSort(List):
    size = len(List)
    if size <=1:
        return List
    for i in range(len(List)-1):
        for j in range(len(List) - 1 - i):
            if List[j] > List[j+1]:
                List[j],List[j + 1] = List[j+1],List[j]
        print('第{}几轮排序结果'.format(i))
        print(List)
    return List

if __name__ == '__main__':
    randomList.randomList(10)
    print(bubbleSort(randomList.randomList(10)))

