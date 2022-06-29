class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1
        cnt = 0
        if s == s[::-1]:
            return True

        while left != right and left < len(s) and right>=0:
            print(str(left)+" "+str(right))
            #print(right)
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                tem, tem2 = s[left+1:right+1], s[left:right]
                return tem == tem[::-1] or tem2 == tem2[::-1]

        return True

ip = "abca"
ip = "aba"
ip = "aab"
ip = "deeee"
print(Solution().validPalindrome(ip))
