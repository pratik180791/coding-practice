
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1


        left = 0
        right = len(nums)-1

        while left<=right:
            mid = left +(right-left) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid]>=nums[left]:
                if  nums[left]<=target<nums[mid]:
                #if target>= nums[left] and target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<target<=nums[right]:
                #if target>nums[mid] and target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1





nums = [4, 5, 6, 7, 0, 1, 2]
nums = [4,5,6,7,0,1,2]
nums = [1,3]
nums = [4,5,6,7,0,1,2]

target = 0
op = Solution().search(nums, 2)
print(op)

"""
def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        elif nums[0] == target:
            return 0
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            
            if target == nums[mid]:
                return mid

            if nums[0] <= target < nums[mid] or 
            target < nums[mid] < nums[0] or
            nums[mid] < nums[0] <= target:
                right = mid-1
            else:
                left = mid+1
        return -1
    
    def _search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        for i, j in enumerate(nums):
            if j == target:
                return i
        return -1"""