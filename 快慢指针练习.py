from typing import List
class Solution:
    def remove(self, nums,val:int):
        s = 0
        f = 0
        while f < len(nums):
            if nums[f] == val:
                f += 1
            else:
                
                nums[s] = nums[f]
                s += 1
                f += 1
        return s
if __name__ == '__main__':
    l = Solution()
    print(l.remove([0,1,2,2,3,0,4,2],2))

