

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted_arr = []
        nums1_cnt , nums2_cnt, j = 0, 0, 0
        min_val = min(m, n)
        if not nums1 and nums2:
            nums1 = nums2
            return

        while j < min_val:
            if nums1[nums1_cnt] < nums2[nums2_cnt] and nums1[nums1_cnt!=0]:
                sorted_arr.append(nums1[nums1_cnt])
                nums1_cnt+=1
                j+=1
            elif nums1[nums1_cnt] > nums2[nums2_cnt] and nums1[nums2_cnt!=0]:
                sorted_arr.append(nums2[nums2_cnt])
                nums2_cnt+=1
                j+=1
            else:
                if nums1[nums1_cnt]!=0:
                    sorted_arr.append(nums1[nums1_cnt])
                    nums1_cnt+=1
                if nums2[nums2_cnt]!=0:
                    sorted_arr.append(nums2[nums2_cnt])
                    nums2_cnt+=1
                j+=1
            print(sorted_arr, nums1_cnt, nums2_cnt, j)


        if nums1_cnt<m:
            for i in range(nums1_cnt, m):
                if nums1[i] == 0:
                    break
                sorted_arr.append(nums1[i])
        else:
            for i in range(nums2_cnt, n):
                if nums2[i] == 0:
                    break
                sorted_arr.append(nums2[i])
        print(sorted_arr)
        nums1 = sorted_arr

Solution().merge(nums1,m,nums2, n)


