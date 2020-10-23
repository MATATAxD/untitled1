from typing import List


def moveZero(nums):
    fast = 0
    slow = 0
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


l = [0, 1, 2, 3, 4, 0]
print(moveZero(l))
