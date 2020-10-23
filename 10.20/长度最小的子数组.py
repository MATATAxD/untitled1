from typing import List


def minSubArrayLen(s: int, nums: List[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    cur = n + 1
    for i in range(n):
        res = 0
        for j in range(i, n):
            res += nums[j]
            if res >= s:
                cur = min(cur, j - i + 1)
                break
    return 0 if cur == n + 1 else cur


l = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(7, l))
