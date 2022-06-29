class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                #temp =
                if s[i] == '+':
                    #print(s[::i-1])
                    #print(s[i + 2::])
                    #tem = s[::i-2] + '--' + s[i+2::]
                    temp = s[:i] + '-' + s[i + 1:]
                    temp = temp[:i+1] + '-' + temp[i + 2:]
                else:
                    temp = s[:i] + '+' + s[i + 1:]
                    temp = temp[:i + 1] + '+' \
                                          '' + temp[i + 2:]
                res.append(temp)
        print(res)
s = "++++"
Solution().generatePossibleNextMoves(s)
