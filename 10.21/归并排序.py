from typing import List
from randomList import randomList


def mergeSort(List):  # 拆
    if len(List) <= 1:
        return List
    middle = len(List) // 2
    left, right = List[0:middle], List[middle:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):  # 合并
    mList = []
    while left and right:
        if left[0] > right[0]:
            mList.append(right.pop(0))
        else:
            mList.append(left.pop(0))
    if left:
        mList.extend(left)
    if right:
        mList.extend(right)

    return mList

def merge1(left,right):  #双指针法
    left_len =len(left)
    right_len = len(right)
    mList = []
    i = 0
    j = 0
    while i < left_len and j < right_len:
        if left[i] < right[j]:
            mList.append(left[i])
            i +=1
        else:
            mList.append(right[j])
            j +=1
    mList.extend(left[i:])
    mList.extend(right[j:])
    return mList





if __name__ == '__main__':
    randomList.randomList(10)
    print(mergeSort(randomList.randomList(10)))
