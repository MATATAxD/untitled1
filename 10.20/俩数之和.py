from  typing import List
def twoSum(nums:List,target:int):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


l = [1,2,3,4,5]
print(twoSum(l,5))