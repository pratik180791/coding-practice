import sys
from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_val = -sys.maxsize
        max_val = sys.maxsize
        return self.isValidBSTWrapper(root, min_val, max_val)

    def isValidBSTWrapper(self, root:Optional[TreeNode], min_val, max_val):
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return self.isValidBSTWrapper(root.right, root.val, max_val) and \
               self.isValidBSTWrapper(root.left, min_val, root.val)

