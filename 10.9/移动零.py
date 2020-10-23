from typing import List

def removezero(nums: List[int]):
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] == 0:
            fast += 1
        else:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    for i in range(slow, len(nums)):
                nums[i] = 0
    return nums

a = [0, 1, 2, 3, 4]
print(removezero(a))
