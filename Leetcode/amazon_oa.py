""""

"""

#from collections import itertools
import itertools



def cntImbal(nums):
    imbal = 0
    if len(nums) ==1:
        return 0
    for i in range(1, len(nums)):
        if nums[i]-nums[i-1]>1:
            imbal+=1
    return imbal


def maxImbalance(ranks):
    combinations = []
    total_imbal = 0
    ranks = sorted(ranks)
    for L in range(0, len(ranks) + 1):
        for subset in itertools.combinations(ranks, L):
            if subset:
                if len(subset) > 1:
                    curr_imbal = cntImbal(subset)
                    print(curr_imbal, subset)
                    total_imbal+=curr_imbal
                combinations.append(subset)

    return total_imbal
nums = [3,1,2]
#op =maxImbalance(nums)
#print(op)



# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findTotalImbalance' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY rank as parameter.
#
def cntImbal(nums):
    imbal = 0
    nums = sorted(nums)
    if len(nums) == 1:
        return 0
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 1:
            imbal += 1
    print(nums, imbal)
    return imbal


def findTotalImbalance(ranks):
    # Write your code here
    # ranks = sorted(ranks)
    # ranks = list(set(ranks))
    # print(ranks
    total_imbal = 0
    visited = set()
    for i in range(0, len(ranks)):
        if ranks[i] in visited:
            continue
        else:
            visited.add(ranks[i])
        for j in range(1, len(ranks) - i + 1):
            combination = ranks[i:i + j]
            total_imbal += cntImbal(combination)
    # print(combinations)

    return total_imbal

nums = [4,4,1,3,2]
op = findTotalImbalance(nums)
print(op)