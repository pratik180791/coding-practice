from typing import List


class Solution(object):
    def _longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre = ""
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        buff = strs[0]
        print(buff)
        for i in strs[1::]:
            temp = ""
            for j in range(len(i)):
                if len(buff[0:j]) <= len(i[0:j]) and i[0:j] == buff[0:j]:
                    temp = i[0:j]
                    print(temp)
            pre = temp
        print(pre)
        return pre

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""

        print(strs)
        for i in range(len(strs[0])):
            c = strs[0][i]
            print(c)
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0] if strs else ""


ip = ["ab", "a"]
ip = ["flower", "flow", "flight"]
#ip = ["flower"]
output = Solution().longestCommonPrefix(ip)
print(output)


