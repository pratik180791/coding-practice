from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        final_res = []
        final_res.append(sorted_intervals[0])
        for i in range(1, len(sorted_intervals)):
            if final_res and final_res[-1][1]>sorted_intervals[i][0]:
                final_res[-1][1] = max(final_res[-1][1], sorted_intervals[i][1])
            else:
                final_res.append(sorted_intervals[i])
        return final_res
ip = [[1,3],[8,10],[2,6],[15,18]]
op = Solution().merge(ip)
print(op)

"""
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6]."""


