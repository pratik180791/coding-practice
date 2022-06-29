a = [1,2,3,4,5,6]

def bin_search(nums, val):
    pos = insert_pos(nums, val)
    print(pos)


def insert_pos(nums, val, left=0, right=None):
    if not left:
        left = 0
    if not right:
        right = len(nums) -1

    while left <= right:
        pivot = (left + right) // 2

        if nums[pivot] > val:
            right = pivot - 1
        elif nums[pivot] < val:
            left = pivot + 1
        else:
            return pivot
    return -1

bin_search(a, 2)

