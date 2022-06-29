from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        for i in range(self.rows):
            for j in range(self.cols):
                #print(self.board[i][j])
                if self.backtrack(i, j, word):
                    return True
        return False

    def backtrack(self, row, col, substring):
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if len(substring) == 0:
            return True

        if row < 0 or self.rows == row or col < 0 \
                or self.cols == col or self.board[row][col] != substring[0]:
            return False

        returned_val = False

        #self.board[row][col] = "$"
        for i in neighbors:
            new_row, new_col = i[0] + row, i[1] + col
            returned_val = self.backtrack(new_row, new_col, substring[1:])
            if returned_val:
                break

        #self.board[row][col] = substring[0]
        return returned_val





ip = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"


op = Solution().exist(ip, word)
print(op)


