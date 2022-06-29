from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for i in matrix:
            res.extend(i)
        print(res)
        return res[k-1]

ip = [[1,5,9],[10,11,13],[12,13,15]]

op = Solution().kthSmallest(ip, 8)
print(op)
