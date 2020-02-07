# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root==None:
            return False
        # if not(root.left and root.right):
        if root.right==None and root.left==None:
            if root.val==sum:
                return True
        a=self.hasPathSum(root.left,sum-root.val)
        print('sum',sum)
        print(1)

        b=self.hasPathSum(root.right,sum-root.val)
        print(2)
        return a or b

    # 层次遍历
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        que=[]
        que.append(root)
        res=[]
        while que:
            num=len(que)
            temp=[]
            while num>0:
                curNode = que.pop(0)
                temp.append(curNode.val)
                if curNode.left:
                    que.append(curNode.left)
                if curNode.right:
                    que.append(curNode.right)
                num-=1
            res.append(temp)
        return res

#      先序遍历
    def preorder(self,root:TreeNode,ans=[])->List[int]:

        if root:
            # 先序遍历
            # ans.append(root.val)
            self.preorder(root.left)
            # 中序遍历
            ans.append(root.val)
            self.preorder(root.right)
            # 后序遍历
            # ans.append(root.val)

        return ans





if __name__ == '__main__':
    data=[5,4,8,11,13,4,7,2,None,None,None,1]
    t=TreeNode(5)
    t4=TreeNode(4)
    t8=TreeNode(8)
    t11=TreeNode(11)
    t13 = TreeNode(13)
    t_4 = TreeNode(4)
    t7 = TreeNode(7)
    t2 = TreeNode(2)
    t1=TreeNode(1)

    t.left=t4
    t.right=t8

    t4.left=t11
    t4.right=None

    t8.left=t13
    t8.right=t_4

    t11.left=t7
    t11.right=t2

    t13.left=t13.right=None

    t_4.right=t1
    t_4.left=None

    s=Solution()
    res= s.hasPathSum(t,22)
    print(res)
    # ans=s.levelOrder(t)
    # print(ans)
    ans1=s.preorder(t)
    print(ans1)



