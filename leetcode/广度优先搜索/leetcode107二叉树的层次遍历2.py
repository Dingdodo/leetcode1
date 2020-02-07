# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if root == None:
            return ans
        if root.left == root.right == None:
            ans.append([root.val])
            return ans
        #  定义队列
        que = []
        que.append(root)
        while len(que)!=0:
            temp=[]
            num=len(que)
            while num>0:
                q=que.pop(0)
                temp.append(q.val)
                if q.left:
                    que.append(q.left)
                if q.right:
                    que.append(q.right)
                num-=1
            ans.append(temp)
        ans.reverse()
        return ans

if __name__ =="__main__":
    a=[2,3,4,1]
    a.reverse()
    print(a)

