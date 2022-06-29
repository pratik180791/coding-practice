ip  = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

from typing import List
class Solution:
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

  def numIslands(self, grid: List[List[str]]) -> int:
    cnt = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == "1":
          self.dfs(grid, i, j)
          cnt += 1
    return cnt
