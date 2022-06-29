from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0]*(cols+1) for _ in range(rows+1)]
        dp1 = [[0]*cols for _ in range(rows)]
        print(dp)
        max_side = 0
        for i in range(rows):
            for j in range(cols):
                # print(matrix[i][j ])
                if matrix[i][j] == "1":
                    #continue
                    #print([i, j])
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1
                    max_side = max(dp[i+1][j+1], max_side)
                #self.find_square(matrix, i, j)
            #print("\n")
        print(dp)
        print(max_side*max_side)


ip = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
ip = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
res = Solution().maximalSquare(ip)
