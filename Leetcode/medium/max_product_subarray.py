from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_till_now = nums[0]
        min_till_now = nums[0]
        res = max_till_now

        for num in range(1, len(nums)):
            i = nums[num]
            temp_max = max(i,
                           max_till_now*i,
                           min_till_now*i
                           )
            min_till_now = min(i,
                               max_till_now*i,
                               min_till_now*i
                               )
            max_till_now = temp_max
            res = max(max_till_now, res)
        return res


ip = [2,3,-2,4]
op = Solution().maxProduct(ip)
print(op)


def maxProduct(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    max_so_far = nums[0]
    min_so_far = nums[0]
    result = max_so_far

    for i in range(1, len(nums)):
        curr = nums[i]
        temp_max = max(curr, max_so_far * curr, min_so_far * curr)
        min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

        max_so_far = temp_max

        result = max(max_so_far, result)

    return result