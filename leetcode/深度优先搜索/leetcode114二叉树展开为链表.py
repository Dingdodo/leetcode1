class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None
        stack = []
        stack.append(root)
        p = root
        while stack:
            cur_node = stack.pop()
            if cur_node != root:
                p.right = cur_node
                p.left = None
                p = p.right

            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)
        return p
