ip = [2,7,11,15]
ip = [2,3,4]
ip = [-1, 0]
"""
inputs are sorted. 
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        if not numbers:
            return result
        left, right = 0, len(numbers)-1
        while left<=right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                return [left+1, right+1]
            elif two_sum<target:
                left+=1
            elif two_sum>target:
                right-=1
        return []


op = Solution().twoSum(ip, -1)
print(op)

1,2,3,4,5





