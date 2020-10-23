from typing import List


class Solution:
    def removezero(self, nums: list[int]) -> None:
        s = 0
        f = 0
        while f < len(nums):
            if nums[f] == 0:
                f += 1
            else:
                nums[s] = nums[f]
                s += 1
                f += 1
        for i in range(s, len(nums)):
            nums[i] = 0


if __name__ == '__main':
    l = Solution
    print(l.removezero([1, 0, 2, 0, 3, 1, 2]))

