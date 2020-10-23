from typing import List

def Search(nums: List, val: int):
    left = 0
    right = len(nums) - 1
    while left <= right:
        if val == nums[left]:   
            return left
        elif val == nums[right]:
            return right
        else:
            mid = (left + right) // 2
            if val < nums[mid]:
                right = mid
            elif val > nums[mid]:
                left = mid
            else:
                return mid


l = list(range(50))
print(Search(l, 27))
