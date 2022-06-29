#Definition for a binary tree node.
from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def __init__(self):
        self.res = []
        self.right_toggle = True
        self.my_queue = deque()

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        self.my_queue.append(root)
        self.traverse_tree(root)
        return self.res

    def traverse_tree(self, root):
        level = 0
        while self.my_queue:
            temp, size = [], len(self.my_queue)
            for i in range(size):
                curr_val = self.my_queue.popleft()
                temp.append(curr_val.val)

                if curr_val.left:
                    self.my_queue.append(curr_val.left)

                if curr_val.right:
                    self.my_queue.append(curr_val.right)

            if level % 2 == 1:
                temp.reverse()

            self.res.append(temp)
            level += 1
