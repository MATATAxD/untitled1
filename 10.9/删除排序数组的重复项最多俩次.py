from typing import List
def reomveElement(nums:List[int])-> int:
    fast = 1
    slow = 0
    count = 1
    while fast < len(nums):
        if nums[fast] == nums[slow]:
            count +=1
            if count == 2:
                slow +=1
                nums[slow] = nums[fast]
            fast +=1
        else:
            slow+=1
            nums[slow] = nums[fast]
            count = 1
            fast +=1
    return slow + 1

a = [1,1,1,2,2,2,3]
print(reomveElement(a))