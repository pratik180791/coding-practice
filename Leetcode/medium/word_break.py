from functools import lru_cache
from typing import List


class Solution:
    def _wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.wordBreakRecur(s, frozenset(wordDict), 0)

    def _wordBreakRecur(self, s, word_dict, start):
        if start == len(s):
            return True

        for end in range(1, len(s)+1):
            if s[start::end] in word_dict and self.wordBreakRecur(s, word_dict, end):
                return True
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        my_words = set(wordDict)
        return self.wordBreakRecur(s, frozenset(wordDict), 0)

   # @lru_cache
    def wordBreakRecur(self, s, word_dict, start):
        if start == len(s):
            return True

        for end in range(1, len(s) + 1):
            if s[start:end] in word_dict and self.wordBreakRecur(s, word_dict, end):
                return True
        return False




s = "leetcode"
wordDict = ["leet", "code"]
#s = "applepenapple"
#wordDict = ["apple", "pen"]
res = Solution().wordBreak(s, wordDict)
print(res)


ab = [1,2]
ab.pop(-1)
print(ab)

# you can write to stdout for debugging purposes, e.g.
print("This is a debug message")
"""

Input: Integer value for e.g. 2 
Output: [Next largest, Next smallest] , list of integers

If not next largest, next smallest
return -1

2: 010


O(n)*(len(max(binary_value)))+O(n)*(len(max(binary_value)))

Traverse from 2 till we get next largest: 
    3=> 011 (total number of 1s = 2) != 1 (len(max(binary_value)))
        keep traversing
    4=> 100 (total 1s)== 1
        append to a list
        break

Traverse from 2 till next lowest:
    1=> 001 ==1
    append
    break

def count_ones(bin_val):
    cnt = 0
    for i in range(int(bin_val)):
        if i==1:
            cnt+=1
    return cnt
fo
"""


