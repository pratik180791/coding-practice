from typing import List

#https://www.youtube.com/watch?v=siKFOI8PNKM
"""
1. Traverse left to right
    Increment up+=1
2. Traverse top to bottom
   Decrement right-=1
3: Traverse right to left
    Decrement bottom
4: Traverse bottom to top
    Increment left 


"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #pass
        res = []
        rows = len(matrix)
        cols = len(matrix[0])
        up = 0
        down = rows - 1
        left = 0
        right = cols - 1
        dir = 0
        while left <= right and up <= down:
            if dir == 0:
                #Traverse Left to right
                #Keep row constant, increment columm value
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up += 1 #To mark the visited
            elif dir == 1:
                #Traverse:
                #up to d
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
            elif dir == 2:
                for j in range(right, left-1, -1):
                    res.append(matrix[down][j])
                down -= 1
            elif dir == 3:
                for k in range(down, up-1, -1):
                    res.append(matrix[k][left])
                left += 1
            dir = (dir+1) % 4
        return res

ip = [[1,2,3],
      [4,5,6],
      [7,8,9]]
res = Solution().spiralOrder(ip)
print(res)
