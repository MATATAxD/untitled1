def longestPalindrome(s: str) -> str:
    for i in range(len(s), -1, -1):
        for j in range(len(s) - i + 1):
            string = s[j:i + j]
            if string == string[::-1]:
                return string

l = 'acbbdc'
print(longestPalindrome(l))