from typing import List
from randomList import randomList


def mergeSort(List):
    if len(List) <= 1:
        return List
    mid = len(List) // 2
    left, right = List[0:mid], List[mid:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
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


if __name__ == '__main__':
    randomList.randomList(10)
    print(mergeSort(randomList.randomList(10)))
