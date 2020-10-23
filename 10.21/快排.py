from typing import List
from randomList import randomList
def quickSort(List,start,end):
    if start >= end:
        return start
    mid = partition(List,start,end)
    quickSort(List,start,mid-1)
    quickSort(List,mid + 1 ,end)


def swap(List,a,b):
    List[a],List[b] = List[b],List[a]

def partition(List,start,end):
    cur = List[start]
    p = start + 1
    q = end
    while p <=q:
        while p <=q and List[p]< cur:
            p +=1
        while p <=q and List[q]>= cur:
            q -=1
        if p<q:
            swap(List,p,q)
    swap(List,start,q)
    return q

l = [1, 3, 4, 6, 7, 9, 10, 24, 5, 8]
quickSort(l, 0, len(l)-1)
print(l)
