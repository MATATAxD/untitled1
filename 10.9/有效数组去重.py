from typing import List

def remove(nums: List[int]) -> int:
    slow = 0
    fast = 1
    while fast < len(nums):
        if nums[fast] == nums[slow]:
            fast += 1
        else:
            slow +=1
            nums[slow] = nums[fast]
            fast += 1
    return slow + 1


a = [1, 1, 2, 3, 4]
print(remove(a))
