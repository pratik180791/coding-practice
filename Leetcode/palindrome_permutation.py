class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        ct = {}

        if s == s[::-1]:
            return True

        ct = Counter(ip)
        ct_new = 0
        for key, val in ct.items():
            ct_new += val % 2
        return ct_new<=1

ip = "carerac"
ip = "abba"
ip = "aba"
ip = "aabbccc"
res = Solution().canPermutePalindrome(ip)
print(res)

from collections import Counter
res = Counter(ip)
print(res)
