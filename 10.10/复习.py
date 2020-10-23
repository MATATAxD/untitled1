from typing import List

def removezere(nums: List[int]):
    fast = 0
    slow = 0
    while fast < len(nums):
        if nums[fast] == 0:
            fast += 1
        else:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    for i in range(slow, len(nums)):
        nums[i] = 0
    return nums

def removeElement(nums:List,val:int):
    fast = 0
    slow = 0
    while fast < len(nums):
        if nums[fast] == val:
            fast += 1
        else:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    return slow
# a = [1,2,3,4,5,6,7]
# print(removeElement(a,1))


def quchong(nums:List[int]):
    slow = 0
    fast = 1
    while fast < len(nums):
        if nums[fast] == nums[slow]:
            fast += 1
        else:
            slow +=1
            nums[slow] = nums[fast]
            fast += 1
    return slow +1
def removeElement(nums:List):
    fast = 1
    slow = 0
    count = 1
    while fast < len(nums):
        if nums[fast] == nums[slow]:
            count += 1
            if count == 2:
                slow += 1
                nums[slow] = nums[fast]
            fast +=1
        else:
            slow +=1
            nums[slow] = nums[fast]
            count = 1
            fast += 1
    return  slow +1






a = [1, 1, 2, 0, 3, 4, 5]
print(quchong(a))


