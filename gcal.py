ip = [[1,4],[0,0]]

st = sorted(ip)
#print(st)

ip = [[1,4],[0,2],[3,5]]


def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    # [1,3] [2,6]
    """
    min = 1
    max = 3
    if a[0]<=max:
    append([min, a[1]])

    """
    result = []
    merged_num = -1
    intervals = sorted(intervals)
    print(intervals)
    for i, j in enumerate(intervals):
        next_num = i + 1
        if i == merged_num:
            merged_num = -1
            continue

        if i == len(intervals) - 1:
            print("here")
            if not result:
                print("here again")
                result.append([j[0], j[1]])
            elif j[0] <= result[-1][1]:
                if j[0] <= result[-1][0]:
                    min_num = j[0]
                else:
                    min_num = result[-1][0]

                if j[1] > result[-1][1]:
                    max_num = j[1]
                else:
                    max_num = result[-1][1]
                print(min_num,max_num)
                result[-1] = [min_num, max_num]
            else:
                result.append([j[0], j[1]])
        elif intervals[next_num][0] <= j[1]:
            if j[0] < intervals[next_num][0]:
                min_num = j[0]
            else:
                min_num = intervals[next_num][0]

            if j[1] > intervals[next_num][1]:
                max_num = j[1]
            else:
                max_num = intervals[next_num][1]

            result.append([min_num, max_num])
            merged_num = next_num
        else:
            result.append([j[0], j[1]])
    return result

ip = [[1,4],[0,2],[3,5]]
exp = [[0,5]]
#ip = [[0, 4], [3, 5]]


def _merge(ip):
    result = []
    ip.sort()
    for j in ip:
        if not result:
            result.append([j[0], j[1]])
        elif j[0] <= result[-1][1]:
            if j[0] <= result[-1][0]:
                min_num = j[0]
            else:
                min_num = result[-1][0]

            if j[1] > result[-1][1]:
                max_num = j[1]
            else:
                max_num = result[-1][1]
            print(min_num, max_num)
            result[-1] = [min_num, max_num]
        else:
            result.append([j[0], j[1]])
    print(result)


ip = [[2,3],[4,5],[6,7],[8,9],[1,10]]
ip = [[1,4],[0,2],[3,5]]
print(_merge(ip))