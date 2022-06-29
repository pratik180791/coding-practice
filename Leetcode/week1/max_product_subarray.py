from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # def maxSub
        total_len = 0

        local_mul = nums[0]
        local_len = 1 if local_mul == 1 else 0
        for i in range(1, len(nums)):
            local_mul *= nums[i]
            print(local_mul, local_len, i)
            if local_mul == 1:
                total_len = max(total_len, local_len)
        return total_len

#nums = [2,3,-2,4]
nums = [1,-1,-1,1,-1,-1]
op = Solution().maxProduct(nums)
print(op)
"""
1 = 1
1, -1 = -1 X
1 -1 -1
"""
print(1*-1*-1*1*1)