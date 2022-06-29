ip = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
op = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]


from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pass

    def dfs(self, grid, row, col):
        rows = len(grid)
        cols = len(grid[0])
        if row < 0 or row >= rows or col >= cols or col < 0 or grid[row][col] == 2 or \
                grid[row][col] == "0":
            return
        grid[row][col] = 2
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row + 1, col)
