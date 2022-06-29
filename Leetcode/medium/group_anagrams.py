ip = ["eat","tea","tan","ate","nat","bat"]
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        op = []
        for i in strs:
            sorted_i = "".join(sorted(i))
            print(sorted_i)
            if sorted_i in res:
                res[sorted_i].append(i)
            else:
                res[sorted_i] = [i]
        print(res)

        for i , j in res.items():
            op.append(j)
        return op

#print(ip)
op = Solution().groupAnagrams(ip)
print(op)

