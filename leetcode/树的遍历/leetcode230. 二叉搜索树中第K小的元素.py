# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root or k<0:
            return
        def helper(root,temp):
            if not root:
                return
            helper(root.left,temp)
            temp.append(root.val)
            helper(root.right,temp)
        res=[]
        helper(root,res)

        return res[k-1]
