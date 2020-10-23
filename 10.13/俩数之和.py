def twosum(nums,target):
    left = 0
    right = len(nums)-1
    nums.sort()
    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            print(nums[left],nums[right])
            left += 1
            right -= 1
        else:
            if curr < target:
                left += 1
            else:
                right -= 1

def twosum1(nums,targrt):
    nums_dict = {}     #存放已遍历值和下标
    for i in range(len(nums)):
        temp = targrt - nums[i]
        if temp  in nums_dict:
            return [i,nums_dict[temp]]
        else:
            nums_dict[nums[i]] = i

def twosum2(nums,target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i , j]
    return []



l=[1,2,3,4,5,6]
print(twosum1(l,6))
