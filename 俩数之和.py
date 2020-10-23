
def twoSum(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            print(nums, [left], nums, [right])
            left+= 1
            right -= 1
        else:
            if curr < target:
                left += 1
            else:
                right -= 1


l = [1, 2, 4, 7, 6,5]
print(twoSum(l,8))
