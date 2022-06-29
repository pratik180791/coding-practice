#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'itemsSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY items as parameter.
#

from collections import Counter

def itemsSort(items):
    if not items:
        return []
    counts = Counter(items)
    new_list = sorted(items, key=lambda x: (counts[x], x))
    return new_list
