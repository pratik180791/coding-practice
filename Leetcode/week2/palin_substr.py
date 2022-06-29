class Solution:
    def _countSubstrings(self, s: str) -> int:
        palin_cnt = 0
        for i in range(len(s)):
            # print(s[i])
            palin_cnt += 1
            for j in range(i + 1, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    # print(s[i:j+1])
                    palin_cnt += 1
        return palin_cnt

    def isPalin(self, s):
        if len(s) == 1:
            return True
        elif len(s) == 2:
            return s[0] == s[1]
        return s==reversed(s)

    def countSubstrings(self, s):
        res = 0
        for i in range(len(s)):
            res+=self.checkPalin(i, i, s)
            res+=self.checkPalin(i, i+1, s)
        return res

    def checkPalin(self, low, high, s):
        res = 0
        while low>=0 and high<len(s):
            if s[low]!=s[high]:
                break
            low+=1
            high-=1
            res+=1
        return res
