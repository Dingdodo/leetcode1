# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 层次遍历要使用队列
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root==None:
            return None
        if root.left==root.right==None:
            return [root.val]
        queue=[]
        queue.append(root)
        ans=[]
        while queue:
            size=len(queue)
            temp=[]
            while size>0:
                curr_node = queue.pop(0)
                temp.append(curr_node.val)
                if curr_node.left!=None:
                    queue.append(curr_node.left)
                if curr_node.right!=None:
                    queue.append(curr_node.right)
                size-=1
            ans.append(temp)
        res=[]
        for a in ans:
            res.append(a[-1])
        return res




