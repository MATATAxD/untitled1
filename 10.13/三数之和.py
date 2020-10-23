from  typing import List
def theresum(nums:List[int]):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                res.append([nums[i],nums[left],nums[right]])
                left += 1
                right -= 1

    return res
l = [1, -1, 2, 0, -2, 2, 3]

print(theresum(l))
