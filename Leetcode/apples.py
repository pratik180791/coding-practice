

def solution(A, K, L):
    max_sum = -1
    if K+L > len(A) or not A:
        return max_sum
    if K>L:
        max_sum_k, k_indexes = helper(A,  K, [])
        max_sum_l, l_indexes = helper(A, L, k_indexes)
    else:
        max_sum_l, l_indexes = helper(A, L, [])
        #print(max_sum_l, l_indexes)
        max_sum_k, k_indexes = helper(A,  K, l_indexes)
        print(max_sum_k, k_indexes, K)
    max_sum = max_sum_l + max_sum_k
    return max_sum


def helper(A, max_items_in_bucket, ignore_range):
    max_a = -1
    index_range = []
    end = len(A)
    for i in range(end):
        bucket_max = i + max_items_in_bucket
        current_sub = A[i:bucket_max]
        print(current_sub)
        curr_sum = sum(current_sub)
        if i in ignore_range:
            continue
        if bucket_max == end + 1 or len(current_sub)!=max_items_in_bucket:
            break
        if curr_sum > max_a:
            max_a = curr_sum
            index_range = [i, bucket_max - 1]
    return max_a, index_range
"""
A= [6,1,4, 6,3, 2,7,4]
k = 3
l = 2
op = solution(A, k, l)
print(op)

A= [10, 19, 15]
k = 2
l = 2
op = solution(A, k, l)
print(op)

A= [5,2,3]
k = 1
l = 2
op = solution(A, k, l)
print(op)

"""
A = [0,6,5,2,2,5,1,9,4]
k = 1
l = 2
op = solution(A, k,l)
print(op)