#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

"""
Step 1: String is balanced/imbalanced 
        1: (()))
        processed_list = []
        i=0, processed_list = [(]
        i=1, processed_list = [(, (]
        i= 2, processedlist = [(]
        i= 3 , processed_list = []
        #i=4, processed_list = []

        )

        if curr_val = ')'


        ()))
        [(]
        []
        []
 Identify the number of missing 
"""


# (((
# )))(((. => cnt=3, len = 3


def getMin(s):
    # Write your code here
    processed_list = []
    cnt = 0
    for i in s:
        if i == "(":
            processed_list.append(i)
        else:
            if not processed_list:
                cnt += 1
            else:
                processed_list.pop()

    return cnt + len(processed_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getMin(s)

    fptr.write(str(result) + '\n')

    fptr.close()
