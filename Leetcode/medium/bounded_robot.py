class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #print(instructions)
        init = [0, 0]
        moves_mapping = [(0, 1), (1, 0), (-1, 0), (0, -1)]  #["UP", "RIGHT", "LEFT", "DOWN"]
        """
        Move left = 3 move right
        
        """
        x = y = 0  #co-ordinates
        index = 0  #magnitude
        res = [init]
        for i in instructions:
            if i == 'L':
                #init = [init[0]-1, init[1]]
                index = (index + 3) % 4
            elif i == 'R':
                #init = [init[0]+1, init[1]]
                index = (index + 1) % 4
            else:
                #init = [init[0], init[1]+1]
                x += moves_mapping[index][0]
                y += moves_mapping[index][1]
            #res.append(init)
            #print(i)
            #print(res)
        return (x,y) == (0,0)

ip = "GL"
res = Solution().isRobotBounded(ip)
print(res)

