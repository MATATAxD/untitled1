from typing import List


def quickSort(List, start, end):
    if start >= end:
        return
    mid = partition(List, start, end)
    quickSort(List, start, mid - 1)
    quickSort(List, mid + 1, end)


def partition(List, start, end):
    cur = List[start]
    marke = start
    for i in range(start + 1, end + 1):
        if List[i] < cur:
            marke += 1
            List[marke], List[i] = List[i], List[marke]
        List[start] = List[marke]
        List[marke] = cur


if __name__ == '__main__':
    l = [1, 3, 4, 6, 7, 9, 10, 24, 5, 8]
    quickSort(l, 0, len(l) - 1)
    print(l)
