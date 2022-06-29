ip = [3,3,3,3,3,1,3]
#groupSizes[1] = 3, then person 1 must be in a group of size 3.

#Output: [[5],[0,1,2],[3,4,6]]
#https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
res = {}
import collections
ct = collections.defaultdict(list)
final = []
for i, j in enumerate(ip):
    if j in res:
        res[j].append(i)
    else:
        res[j] = [i]
    if len(res[j]) == j:
        final.append(res[j])
        del res[j]
sorted(final)
print(final)

