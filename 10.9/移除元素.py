from typing import List
def removeElement(nums:List[int],val:int)->int:
    fast = 0
    slow = 0
    while fast < len(nums):
        if nums[fast]== val:
            fast +=1
        else:
            nums[slow] = nums [fast]
            slow +=1
            fast +=1
    return slow

a = [1,2,3,4,5,6]
print(removeElement(a,1))