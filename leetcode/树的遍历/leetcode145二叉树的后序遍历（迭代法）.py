from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 方法一 一个栈就可以了
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[]
        res=[]
        if root==None:
            return []
        stack.append(root)

        while stack:
            cur_node=stack.pop()
            res.append(cur_node.val)
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
        res=reversed(res)

        return res

