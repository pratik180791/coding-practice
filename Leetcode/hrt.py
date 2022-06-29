from typing import List

def maxSubArray(nums: List[int]) -> int:
    local_max = nums[0]
    #total_max = nums[0]
    max_sub = 0
    #print(local_max)
    for i in range(1, len(nums)):
        local_max = local_max & nums[i]
        if local_max > 0:
            max_sub += 1
        else:
            local_max = nums[i]
        #print(local_max)
    return max_sub


nums = [13, 7, 2, 8, 3]
op = maxSubArray(nums)
print(op)
print(13&7&3)

num1 = [1, 0, 0]
num2 = [1, 1, 1]
#print(num1|num2)
num = 100111
print(int(num))