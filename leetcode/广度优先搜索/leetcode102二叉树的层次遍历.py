# Definition for a binary tree node.
from typing import List
import math

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans=[]
        if root == None:
            return ans
        if root.left==root.right ==None:
            ans.append([root.val])
            return ans
        #  定义队列
        que=[]
        que.append(root)

        while len(que)!=0:
            num=len(que)
            temp = []
            while num>0:
                q=que.pop(0)
                temp.append(q.val)
                if q.left!=None:
                    que.append(q.left)
                if q.right:
                    que.append(q.right)

                num-=1
            ans.append(temp)

        return ans


if __name__=="__main__":
   t=[]
   t.append(1)
   t.append(2)
   print(t.pop(0))
   print(t.pop(0))










