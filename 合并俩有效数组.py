from typing import List


def Two(nums1: List[int], m: int, nums2: List[int], n: int):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
    if j >= 0:
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


l = [1, 2, 3, 4]
p = [5, 6]

print(Two(l, 3, p, 2))
