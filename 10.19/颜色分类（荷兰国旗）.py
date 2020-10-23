from typing import List
def sortColors(nums:List):
    head = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i],nums[head] = nums[head],nums[i]
            head +=1
    for i in range(head,len(nums)):
        if nums[i] == 1:
            nums[i],nums[head] = nums [head],nums[i]
            head +=1
    return nums

l = [2,0,2,1,1,0,2,1,0]
print(sortColors(l))