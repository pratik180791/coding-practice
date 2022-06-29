from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        columns = len(grid[0])

        # initialise visited matrix
        count = 0

        def dfs(start, end):
            if start >= rows or end >= columns or start < 0 or end < 0 or \
                    grid[start][end] == 2 or grid[start][end] == "0":
                return
            grid[start][end] = 2
            dfs(start, end + 1)
            dfs(start, end - 1)
            dfs(start - 1, end)
            dfs(start + 1, end)

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        print(count)
        return count

