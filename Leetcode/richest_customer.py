from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_val = 0
        max_ind = -1
        for i, j in enumerate(accounts):
            for k in j:
                if sum(j)>max_val:
                    max_val = sum(j)
                    max_ind = i


        print(max_ind, max_val)
        return max_val


accounts = [[1, 2, 3], [3, 2, 1]]
res = Solution().maximumWealth(accounts)
print(res)
