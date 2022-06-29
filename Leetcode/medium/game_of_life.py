from typing import List
import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = []

        rows = len(board)
        cols = len(board[0])
        new_board = copy.deepcopy(board)
        for i in range(rows):
            for j in range(cols):
                board[i][j] = self.alive_or_dead(i, j, new_board)

        print(board)

    def alive_or_dead(self, row, col, board):
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0),
                     (1, 1), (-1, -1), (-1, 1), (1, -1)
                     ]
        alive_cnt = 0
        dead_cnt = 0
        for i in neighbors:
            new_row, new_col = row+i[0], col+i[1]
            if not ((0 <= new_row < len(board)) and (0 <= new_col < len(board[0]))):
                continue

            neighbor_val = board[new_row][new_col]
            if neighbor_val == 1:
                alive_cnt += 1
            else:
                dead_cnt += 1

        if board[row][col] == 1 and (alive_cnt < 2 or alive_cnt > 3):
            return 0

        if board[row][col] == 1 and alive_cnt in (2, 3):
            return 1

        if board[row][col] == 0 and alive_cnt == 3:
            return 1
        return board[row][col]

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
expected_op = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Solution().gameOfLife(board)
"""
Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
"""