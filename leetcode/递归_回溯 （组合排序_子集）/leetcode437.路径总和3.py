# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    step = 0
    temp = 0

    def pathSum(self: int, root: TreeNode, sum1: int) -> int:
        if not root:
            return 0
        self.helper(root, sum1)
        self.pathSum(root.left, sum1)
        self.pathSum(root.right, sum1)
        return self.step
    def helper(self, root, sum1):
        if not root:
            return
        if root.val == sum1:
            self.step += 1
        self.helper(root.left, sum1 - root.val)
        self.helper(root.right, sum1 - root.val)