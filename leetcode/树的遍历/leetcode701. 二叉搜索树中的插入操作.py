# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        def helper(root,val):
            if root.right==root.left==None:
                if root.val<val:
                    root.right=TreeNode(val)
                elif root.val>val:
                    root.left=TreeNode(val)
                return
            if root.left==None and root.val>val:
                root.left=TreeNode(val)
                return
            if root.right==None and root.val<val:
                root.right=TreeNode(val)
                return
            elif root.val>val:
                  helper(root.left,val)
            else:
                 helper(root.right,val)
        helper(root,val)
        return root

    # 方法二
    def insertIntoBST1(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root


