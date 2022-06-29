from typing import List

nums = [1, 2, 3,4,5,6, 6]
k = 12



#op 2
nums = [1,2,3,4,5,6,7,1,23,21,3,1,2,1,1,1,1,1,12,2,3,2,3,2,2]
k = 32
nums = [1,-1,0]
k = 0
#0: 1 => 32 NO
""""
arr = [[1,2, 3, 4, 5 , 6,7 ] 
1 is 1<32,yes
2 2+1<=32 yes
3 1+2+3<=32 yes
4 1+2+3+4<=32 10<32 yes
5 1+2+3+4+5<=32 15<=32 ye
6 1+2+3+4+5+6<=32 21<32 yes
7 1...+7<=32 i.e. 28<32 yes 
1 1....+8 29<=32 nO break

32-1 => 31
32-2 => 30
32->3

2
"""
def subarraySum(nums: List[int], k: int) -> int:
        n = len(nums)
        all_arrs = 0
        arrs = []
        for i in range(n):
            temp_sum = nums[i]
            if temp_sum == k:
                arrs.append(nums)
                all_arrs+=1
            for j in range(i + 1, n):
                temp_sum += nums[j]
                if temp_sum == k:
                    arrs.append(nums[i:j])
                    all_arrs += 1
                    #break
        print(arrs)
        return all_arrs

def sub_sum(nums, k):
    slow = 0
    mapper = {}
    mapper[0] = 1
    cum_sum = 0
    cnt = 0
    for i in range(len(nums)):
        cum_sum += nums[i]
        if cum_sum-k in mapper:
            cnt += mapper.get(cum_sum-k)
        mapper[cum_sum] = mapper.get(cum_sum, 0) + 1
    print(mapper)
    return cnt




print(nums)
op = subarraySum(nums, k)
print(op)
op = sub_sum(nums, k)
print(op)

from collections import defaultdict
a = defaultdict(int)
a.get(0)
print(a.get(0))
print("A")