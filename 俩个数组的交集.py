from typing import List
def intersection(nums1:List[int],nums2:List[int]):
    nums1.sort()
    nums2.sort()
    i=0
    j=0
    nums_set=set()
    while i<len(nums1)and j<len(nums2):
        if nums1[i]>nums2[j]:
            j+=1
        elif nums1[i]<nums2[j]:
            i+=1
        elif nums1[i]==nums2[j]:
            nums_set.add(nums1[i])
            j+=1
            i+=1
        return list(nums_set)
nums1=[4,9,7]
nums2=[9,4,9,6,4]
print(intersection(nums1,nums2))


