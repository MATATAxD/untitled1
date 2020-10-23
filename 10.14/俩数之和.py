def twosums(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def twosums1(nums, target):
    nums_dict = {}
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in nums_dict:
            return [i, nums_dict[temp]]
        else:
            nums_dict[nums[i]] = i
