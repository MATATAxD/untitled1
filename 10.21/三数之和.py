def theresum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        if i >0 and nums[i] == nums[i-1]:
            continue
        left=i+1
        right=len(nums)-1


