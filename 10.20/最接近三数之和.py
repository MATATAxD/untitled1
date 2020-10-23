from typing import List


def threeSumClosest(nums: List[int], target: int):    #固定一个值找另外俩个值双指针
    nums.sort()
    res = float('inf')
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            cur = nums[i] + nums[left] + nums[right]
            if cur == target:
                return target
            if abs(res - target) > abs(cur - target):
                res = cur
            if cur > target:
                right -= 1
            elif cur < target:
                left += 1
    return res

l= [-1,2,1,-4]
print(threeSumClosest(l,1))