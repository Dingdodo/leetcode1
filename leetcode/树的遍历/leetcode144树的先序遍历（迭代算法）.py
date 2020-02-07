# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Tree_Method:
    def creatTree(self,arr):
        length=len(arr)

        root=TreeNode(arr[0])
        if length>=2:
            root.left=self.creatTree(arr[1])
        if length>=3:
            root.right=self.creatTree(arr[2])
        return root

# 深度遍历 用栈
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        stack=[]
        stack.append(root)
        res=[]
        while stack:
            cur_treeNode=stack.pop()
            res.append(cur_treeNode)
            # 先进右节点

            if cur_treeNode.right:
                stack.append(cur_treeNode.right)
            if cur_treeNode.left:
                stack.append(cur_treeNode.left)
        return res

if __name__ == '__main__':
     a=[1,2,3]