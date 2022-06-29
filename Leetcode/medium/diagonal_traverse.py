nums = [[1,2,3],[4,5,6],[7,8,9]]
nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
nums = [[1,2,3,4,5,6]]
nums = [[6],[8],[6,1,6,16]]


class Diagnoal:
    def __init__(self):
        self.result = []
        self.visited = []

    def diagonal_traverse(self, nums):
        rows = len(nums)
        cols = len(nums[0])
        if len(nums) == 1:
            return nums[0]

        for i in range(rows):
            for j in range(len(nums[i])):
                self.traverse(nums, i, j)
                #print((i,j))
                #print(self.result)
                if i == rows - 1:
                    print(i, j)
                    continue
                break
        print(self.result)
        return self.result

    def traverse(self, nums, row, col):
        #if not (0 <= row < len(nums) or 0 <= col < len(nums[0])):
        print(row, col)
        if row < 0 or row >= len(nums) or col < 0 or col >= len(nums):
            return
        visited_key = str(row)+str(col)
        if visited_key in self.visited:
            return

        self.visited.append(visited_key)
        #print(row, col)
        #print(self.result)
        if 0 <= col<len(nums[row]):
            self.result.append(nums[row][col])

        diag_x, diag_y = row - 1, col + 1
        self.traverse(nums, diag_x, diag_y)

Diagnoal().diagonal_traverse(nums)
row = -1
col = 1

