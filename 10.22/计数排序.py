from typing import List
from randomList import randomList


def countSort(List):
    if len(List) <= 1:
        return List
    maxv = max(List)
    count_list = [0] * (maxv + 1)
    for i in range(len(List)):
        count_list[List[i]] += 1
    sort_list = []
    for i in range(len(count_list)):
        for j in range(count_list[i]):
            sort_list.append(i)
    return sort_list


l = [1, 1, 2, 4, 4, 2, 3, 5, 7, 8, 9, 8]
print(countSort(l))
