#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMaxColors' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER money
#

def getMaxColors(prices, money):
    return max_length(prices, money)


def max_length(s, k):
    subarray_start = 0
    subarray_end = 0

    subarray_sum = 0
    max_len = -1
    for i in s:
        subarray_sum += i
        subarray_end += 1
        while subarray_sum > k:
            subarray_sum -= s[subarray_start]
            subarray_start += 1

        max_len = max(max_len, subarray_end - subarray_start)

    return max_len


#Social network problem
