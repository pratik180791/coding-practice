from collections import defaultdict
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        mapper = {}
        result = []
        if not items:
            return items
        for i in items:
            #print(i)
            if i[0] in mapper:
                mapper[i[0]].append(i[1])
            else:
                mapper[i[0]] = [i[1]]

        for i, j in mapper.items():
            j.sort(reverse=True)
            result.append([i, int(sum(j[:5])/5)])

        print(mapper)
        return sorted(result, key=lambda x: x[0])
        #print(result)

        #return result


ip = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
ip = [[5,91],[5,92],[3,93],[3,97],[5,60],[3,77],[5,65],[5,87],[5,100],[3,100],[3,76]]
print(defaultdict(list))
res = Solution().highFive(ip)
print(res)
#sorted(result, key=lambda x: x[0])
#res.highFive(ip)
temp = [1,2,3,4]
#print(temp[:2])