ip  = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
from collections import deque

from typing import List
class Solution:
  def dfs(self, grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0,1), (0, -1), (-1, 0), (1, 0)]

    if row < 0 or row >= rows or col >= cols or col < 0 or grid[row][col] == 2 or \
            grid[row][col] == "0":
      return

    grid[row][col] = 2
    for i in directions:
      self.dfs(grid, i[0], i[1])
    """
    self.dfs(grid, row, col + 1)
    self.dfs(grid, row, col - 1)
    self.dfs(grid, row - 1, col)
    self.dfs(grid, row + 1, col)
    """
  def bfs(self, grid, row, col):
    my_queue = deque()
    my_queue.append((row, col))
    grid[row][col] = 2
    rows = len(grid)
    cols = len(grid[0])
    while my_queue:
      i, j = my_queue.popleft()
      directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
      for di, dj in directions:
        rc, cc = di+i, dj+j
        if rc > 0 or rc < rows or cc < cols or cc > 0 or grid[row][col] == 2 or \
                grid[rc][cc] == "0":
          my_queue.append((rc, cc))
          grid[rc][cc] = 2




  def numIslands(self, grid: List[List[str]]) -> int:
    cnt = 0
    rows = len(grid)
    cols = len(grid[0])

    if not grid or len(grid) == 0:
      return cnt
    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == "1":
          self.bfs(grid, i, j)
          cnt += 1
    return cnt
