ip = [1,8,6,2,5,4,8,3,7]
#height = [1,1]
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        areas = []
        left = 0
        right = len(height)-1
        max_area = -1
        while left<right:
            curr_area = (right-left)*min(height[right], height[left])
            print(curr_area)
            max_area = max(curr_area, max_area)
            if height[left]<height[right]:#and left+1<len(height):
                left+=1
            else: #height[right]<=height[left]:# and right-1>0:
                right-=1
            #left+=1
            #left+=1
            #right-=1
        return max_area
op = Solution().maxArea(ip)
print(op)
#op = Solution().maxArea([1,1])
#print(op)
ip = [3, 9,3,4,7,2,12,6]
op = Solution().maxArea(ip)
print(op)
""""
0  = 3
7 = 6

Area = 3*7

1 = 9
6 = 12
Area = 5*9

"""