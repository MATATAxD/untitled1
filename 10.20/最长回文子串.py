from typing import List


def longestPalindrome(strs: str):
    lenth = len(strs)
    if lenth < 2:
        return strs
    maxlen = 1
    res = strs[0]
    for i in range(lenth - 1):
        odd = centersSpread(strs, i, i)
        even = centersSpread(strs, i, i + 1)
        maxstr = odd if len(odd) > len(even) else even
        if len(maxstr) > maxlen:
            maxlen = len(maxstr)
            res = maxstr
    return res


def centersSpread(strs: str, left: int, right: int):
    i = left
    j = right
    length = len(strs)
    while i >= 0 and j < length:
        if strs[i] == strs[j]:
            i -= 1
            j += 1
        else:
            break
    return strs[i + 1:j]


if __name__ == '__main__':
    l = 'acbbdc'
    print(longestPalindrome(l))
