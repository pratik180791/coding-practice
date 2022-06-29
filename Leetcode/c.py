# ip = [4,5,6,5,4,3]
# from collections import Counter
# a = Counter(ip)
# print(a)
# ip = {k: v for k, v in sorted(a.items(), key=lambda item: item[1])}
# print(ip)
# ip = {k: v for k, v in sorted(a.items(), key=lambda item: item[0])}
# print(ip)
#
# lst = [4,5,6,5,4,3]
# counts = Counter(lst)
# new_list = sorted(lst, key=lambda x: (counts[x], x))
# print(new_list)
#
# ip_list = [2,3,5,1,1,2,1]
# money = 7
#
# for i in ip_list:
def printSubArrays(arr, start, end):
    # Stop if we have reached the end of the array
    if end == len(arr):
        return

    # Increment the end point and start from 0
    elif start > end:
        return printSubArrays(arr, 0, end + 1)

    # Print the subarray and increment the starting
    # point
    else:
        print(arr[start:end + 1])
        return printSubArrays(arr, start + 1, end)


# Driver code
arr = [1, 2, 3]
ip_list = [2,3,5,1,1,2,1]
printSubArrays(ip_list, 0, 0)