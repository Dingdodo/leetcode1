# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def helper(root1,root2):
            if not(root1 and root2):
                return True
            if not(root1 or root2):
                return False
            if root1.val!=root2.val:
                return False
            return helper(root1.left,root2.right) and helper(root1.right,root2.left)
        return helper(root,root)




