ip = [-1,0,1,2,-1,-4]
#ip = [1,2,-2,-1]
mapper = {}
result = []
for i in range(len(ip)):
    if ip[i] in mapper:
        mapped_result = mapper[ip[i]]
        num1_key = list(mapped_result[0].items())[0][0]
        num2_key = list(mapped_result[1].items())[0][0]
        #print(i, num2_key, num1_key)
        if i != num1_key and i != num2_key:
            temp_result = sorted([ip[i], list(mapped_result[0].values())[0],
                                  list(mapped_result[1].values())[0]])
            if temp_result not in result:
                result.append(temp_result)
    for j in range(i+1, len(ip)):
        diff = ip[i]+ip[j]
        num1 = {i: ip[i]}
        num2 = {j: ip[j]}
        mapper.update({-diff: [num1, num2]})

#print(mapper)
# print(result)
from typing import List
class Solution:
    def __init__(self):
        self.result = []

    def twoSum(self, numbers: List[int], curr_pos):
        left, right = curr_pos+1, len(numbers) - 1
        print(left, right)

        while left < right:
            two_sum = numbers[left] + numbers[right] + numbers[curr_pos]
            if two_sum == 0:
                self.result.append([numbers[left] ,
                                    numbers[right],
                                    numbers[curr_pos]
                                    ])
                left+=1
                right-=1
                while left<right and numbers[left] == numbers[left-1]:
                    left+=1
            elif two_sum < 0:
                left += 1
            else:
                right -= 1

    def threeSum(self, ip: List[int]) -> List[List[int]]:
        ip = sorted(ip)
        for i in range(len(ip)):
            if ip[i]>0:
                """
                Because we are sorting the list, if we reach value greater than 0
                All values after current will be >0
                """
                break

            if i == 0 or ip[i] != ip[i-1]:
                self.twoSum(numbers=ip, curr_pos=i)
        return self.result

ip = [-1,0,1,2,-1,-4]
res = Solution().threeSum(ip)
print(res)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1