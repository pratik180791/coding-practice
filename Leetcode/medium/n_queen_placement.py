class NQueen:
    def __init__(self):
        pass

    def totalNQueens(self, n: int) -> int:
        self.rows = [0] * n
        self.hills, self.slopes = [0] * (2 * n - 1), \
                                  [0] * (2 * n - 1) #TODO: Need to understand why
        self.n = n

        return self.backtrack()

    def is_not_under_attack(self, row, col):
        return not (self.rows[col] or self.hills[row-col] or self.slopes[row+col])

    def place_queen(self, row, col):
        self.rows[col] = 1
        self.hills[row - col] = 1
        self.slopes[row + col] = 1

    def remove_queen(self, row, col):
        self.rows[col] = 0
        self.hills[row - col] = 0
        self.slopes[row + col] = 0

    def backtrack(self, row=0, count=0):
        for col in range(self.n):
            if self.is_not_under_attack(row, col):
                self.place_queen(row, col)
                if row+1 == self.n:
                    count += 1
                else:
                    count = self.backtrack(row+1, count)
                self.remove_queen(row, col)
        return count


nq = NQueen()
op = nq.totalNQueens(4)
print(nq.hills)


print(op)








