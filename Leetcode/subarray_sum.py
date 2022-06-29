def sub_array_sum(nums, k):
    n = len(nums)
    all_arrs = 0
    arrs = []
    for i in range(n):
        temp_sum = nums[i]
        for j in range(i + 1, n):
            temp_sum += nums[j]
            print(i, j)
            if temp_sum == k:
                arrs.append(nums[i:j+1])
                all_arrs += 1
            elif temp_sum > n:
                break
    print(arrs)
    return all_arrs


nums = [1, 1,1]
nums = [1,2,1,2,1]
nums = [1,2,3]
k = 3
nums = [8, 5, 9, 10, 5, 6, 21, 8]
op = sub_array_sum(nums, k)
print(op)

