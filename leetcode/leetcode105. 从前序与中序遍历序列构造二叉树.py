# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not (preorder or inorder):
            return
        x=preorder.pop(0)
        root=TreeNode(x)
        i=inorder.index(x)
        root.left=self.buildTree(preorder[:i],inorder[:i])
        root.right=self.buildTree(preorder[i+1:],inorder[i+1:])
        return root

if __name__ == '__main__':
    nums=[1,4,5]
    print(nums.pop(-1))
    print(nums)
    print(nums.index(4))