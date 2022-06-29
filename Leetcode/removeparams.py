class Solution(object):
    def minRemoveToMakeValid(self, s):
        open_par = []
        s = list(s)

        for idc, char in enumerate(s):
            if char == '(':
                open_par.append(idc)
            elif char == ')':
                if open_par:
                    open_par.pop()
                else:
                    s[idc] = ""

        while open_par:
            s[open_par.pop()] = ""

        return "".join(s)

    def _minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        params = []
        res = ""
        temp = [i for i in s]
        opening_bracs , closing_bracs = 0, 0
        balance = ""
        for i, j in enumerate(s):
            if j == ')':
                if params:
                    params.pop()
                    res+=j
                closing_bracs+=1
            elif j == '(':
                params.append(j)
                res+=j
                opening_bracs+=1
            else:
                res+=j
       # print(res)
       # print(params)
        if opening_bracs==closing_bracs:
            return res

        tempres = ""
        params = []
        for i, j in enumerate(reversed(res)):
            if j == '(':
                if params:
                    params.pop()
                    tempres += j
            elif j == ')':
                params.append(j)
                tempres += j
            else:
                print("here")
                tempres += j
        print(tempres)

ip = "lee(t(c)o)de)"
ip = "))(("
print(ip)
ret = Solution().minRemoveToMakeValid(ip)
print(ret)
ip = "lee(t(c)o)de)"
ret = Solution().minRemoveToMakeValid(ip)
print(ret)
a = []

