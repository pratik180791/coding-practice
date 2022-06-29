from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        elif nums[0] == target:
            return 0
        #mid =
        #return self.find(0, len(nums)-1, (0+len(nums)-1)//2, nums, target)

        #print()
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            #print("I am here")
            #print(mid)
            if target == nums[mid]:
                return mid

            if nums[0] <= target < nums[mid] or target < nums[mid] < nums[0]:
                    #nums[mid] < nums[0] <= target:
                #left = mid+1
                right = mid-1
            else:
                left = mid+1
        return -1


    def _find(self, left, right, mid, nums, target):
        #mid = left

        if target == nums[left]:
            return left
        elif target == nums[right]:
            return right
        elif target == nums[mid]:
            return mid

        #mid = (0 + len(nums) - 1) // 2
        # print(mid)
        #left = 0
        if target >= left > 0:
            left = mid + 1
        elif target <= mid and right < len(nums):
            right = mid
        else:
            return -1
        mid = (left+right)//2
        self.find(left, right, mid, nums, target)



ip = [4,5,6,7,0,1,2]
res = Solution().search(ip, 0)
print(res)


