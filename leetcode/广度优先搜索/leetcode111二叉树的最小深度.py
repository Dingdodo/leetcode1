# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        h = 0
        if root == None:
            return 0

        #  定义队列
        que = []
        que.append(root)
        while len(que)!=0:

            num=len(que)
            h+=1
            while num>0:
                q=que.pop(0)
                if q.right==None and q.left==None:
                    return h
                if q.left:
                    que.append(q.left)
                if q.right:
                    que.append(q.right)
                num-=1


if __name__ =="__main__":
    a=[2,3,4,1]
    a.reverse()
    print(a)

