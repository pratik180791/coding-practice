class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not nums1:
            return nums2
        if not nums2:
            return nums1

        res = []
        num1cnt = 0
        num2cnt = 0
        for i in range(m + n):
            if num1cnt == m and num2cnt < n:
                res.extend(nums2[num2cnt:])
                print("HERE")
                print(num1cnt)
                break
            if num2cnt == m and num1cnt < n:
                res.extend(nums1)
                print("NO HERE")
                break
            if nums1[num1cnt] < nums2[num2cnt]:
                res.append(nums1[num1cnt])
                num1cnt += 1
            elif nums2[num2cnt] < nums1[num1cnt]:
                res.append(nums2[num2cnt])
                num2cnt += 1
            else:
                res.append(nums2[num2cnt])
                res.append(nums1[num1cnt])
                num2cnt += 1
                num1cnt += 1
            print(res)
        return res
        print(res)
nums1  = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

Solution().merge(nums1, m, nums2, n)
