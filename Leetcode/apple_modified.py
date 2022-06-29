def solution(A, k, l):
    cum_arr = A
    if k+l > len(A) or not A:
        return -1
    for i in range(1, len(A)):
        cum_arr[i] += cum_arr[i - 1]
    print(cum_arr)
    k_max = cum_arr[k - 1]
    l_max = cum_arr[l - 1]
    print(k_max, l_max)
    total_apple_basket = k + l
    max_apples = A[k + l - 1]
    for i in range(total_apple_basket, len(A)):
        k_max = max(k_max, A[i - l] - A[i - l - k])
        l_max = max(l_max, A[i - k] - A[i - l - k])
        max_apples = max(max_apples, k_max + A[i] - A[i - l],
                         l_max + A[i] - A[i - k])
    return max_apples

#A = [0,6,5,2,2,5,1,9,4]
#k = 1
#l = 2

A = [6, 1, 4, 6, 3, 2, 7, 4]
k = 3
l = 2
A = [10, 19, 15]
k = 2
l = 2
op = solution(A, k, l)
print(op)
