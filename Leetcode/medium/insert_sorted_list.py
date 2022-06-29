ip = [1,2,3,4]

n = 5
from typing import List


def bin_insert(num, result_list: List):
    index = -1
    for i in range(len(result_list)):
        if result_list[i]>n:
            index = i
            break

    result_list = result_list[::index] + [num] + result_list[index:]
    print(result_list)



def insort_insert(result:List,num, low=0, high=None):
    pos = get_insert_position(result, num, low, high)
    print(pos)
    result.insert(pos, num)
    print(result)

def get_insert_position(result, num, low=0, high=None):
    if low<0:
        raise ValueError("Blas")
    if high is None:
        high = len(result)
    while low<high:
        pivot = (low+high)//2
        if num < result[pivot]:
            high = pivot
        else:
            low = pivot+1
    return low

insort_insert(ip, 2)
