nums = [4, 5, 6, 7, 8, 1, 2, 3]


def get_pivot(left, right):
    if nums[left] < nums[right]:
        return 0
    while left <= right:
        pivot = (left+right)//2
        if nums[pivot] > nums[pivot+1]:
            return pivot+1
        else:
            if nums[pivot] < nums[left]:
                right = pivot-1
            else:
                left = pivot+1

def binary_search(_left, _right, target):
    while _left <= _right:
        pivot = (_left + _right) // 2
        if target == nums[pivot]:
            return pivot
        else:
            if target > nums[pivot]:
                _left = pivot+1
            else:
                _right = pivot-1
    return  -1


lef = 0
righ = len(nums)-1
target = 4
pivot = get_pivot(lef, righ)
print(pivot)

if target == nums[pivot]:
    res = pivot
elif pivot == 0:
    res = binary_search(0, len(nums) - 1, target)
elif target>nums[pivot]:
    print("here")
    res = binary_search(0, pivot, target)
elif target<nums[pivot]:
    res = binary_search(pivot, len(nums)-1, target)

print(res)

#print(pivot)


from collections import defaultdict

mapper = defaultdict(int)

op = mapper.get("A")
op = mapper.get(1)
print(op)
