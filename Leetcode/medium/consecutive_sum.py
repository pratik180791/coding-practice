n = 9


def consecutive_sum(n):
    nums = []
    nums.append([n])
    ip_nums = [i for i in range(1, n + 1)]
    #print(ip_nums)
    if not n or n < 0:
        return 0

    for i in range(1, n + 1):
        temp_sum = i
        for j in range(i + 1, n + 1):
            temp_sum += j
            if temp_sum == n:
                nums.append(ip_nums[i - 1:j])
                break
            elif temp_sum > n:
                break
    print(nums)
    return len(nums)
#consecutive_sum(9)
from datetime import datetime
print(datetime.now())
op = consecutive_sum(15)
#op = consecutive_sum(8504986)
print(op)
print(datetime.now())


def consecutiveNumbersSum(N):
    print(datetime.now())
    res = 1
    i = 3
    while N % 2 == 0:
        N /= 2
    print(N)
    while i * i <= N:
        count = 0
        while N % i == 0:
            N /= i
            count += 1
        res *= count + 1
        i += 2
    print(datetime.now())
    return res if N == 1 else res * 2

#op = consecutiveNumbersSum(15)
op = consecutiveNumbersSum(8)
print(op)



