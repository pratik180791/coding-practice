from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        min_val = -1
        while left<right:
            mid = (left + right) // 2
#            print(nums[left], nums[mid], nums[right])
            if nums[right]<nums[mid]:
                #print("here")
                left = mid+1
            else:
                #min_val = nums[mid]
                right = mid
                #print(min_val)
                #return min_val
        return nums[left]
ip = [3,4,5,1,2]
Solution().findMin(ip)