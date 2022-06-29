ip = [40, 90, 30, 20, 110, 130, 80, 90]

stack = []
d = {}

def dailyTemperatures(nums):
    res = [-1] * len(nums)
    stack = []  # indexes from hottest to coldest
    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[i] >= nums[stack[-1]]:
            stack.pop()  # remove lower and not soonest
        if stack:
            res[i] = stack[-1] - i
        stack.append(i)
    return res


op = dailyTemperatures(ip)
print(op)
