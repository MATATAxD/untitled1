from typing import List


def hanmingzonghe(nums: List[int]):
    res = 0
    for i in range(32):
        count_0 = 0
        count_1 = 0
        for j in range(len(nums)):
            if(nums[j] >> i) & 1:
                count_1 += 1
            else:
                count_0 += 1

        res = res + count_0 * count_1
    return res

if __name__ == '__main__':
    l = [4, 14, 2]
print(hanmingzonghe(l))
