class Solution:
    def isSubtree(self, s, t) -> bool:
        temp = []

        def traverse(s):
            if s:
                return f"#{s.val}{traverse(s.left)}{traverse(s.right)}"

        a = traverse(t)
        print(a)
        return a in traverse(s)

        def traverse(node):
            if node: return f"#{node.val}{traverse(node.left)}{traverse(node.right)}"

        return traverse(t) in traverse(s)
