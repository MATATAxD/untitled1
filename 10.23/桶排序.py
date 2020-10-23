from typing import List
from randomList import randomList


def buckerSort(List):
    if len(List) <= 1:
        return List
    max_value = max(List)
    min_value = min(List)
    d = max_value - min_value
    buckers = len(List)  # 桶的个数
    count_list = []  # 空桶
    for i in range(buckers):  # 造桶
        count_list.append([])

    for i in range(len(List)):  # 定位元素属于哪个桶子
        num = int((List[i] - min_value) * (buckers - 1) / d)
        bucker = count_list[num]
        bucker.append(List[i])

    for i in range(len(count_list)):  # 每个桶子内部排序
        count_list[i].sort()

    sort_List = []   #按顺序输出ng
    for i in count_list:
        for j in i:
            sort_List.append(j)
    return sort_List


if __name__ == '__main__':
    randomList.randomList(10)
    print(buckerSort(randomList.randomList(10)))
