from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return
        def preorder(root : TreeNode,temp:List):
            if not root:
                return
            if root.right==None and root.left==None:
                temp=temp*10+root.val
            preorder(root.left,10*temp+root.val)
            preorder(root.right,10*temp+root.val)
        res=0
        preorder(root,res)
        return res

        # resSum=[]
        # for list in res:
        #     sum1=0
        #     for i in range(len(list)):
        #         sum1+=(list[i]*(10**(len(list)-1-i)))
        #     resSum.append(sum1)
        # return sum(resSum)











if __name__ == '__main__':
    resSum = []
    res=[[1,2],[1,3]]
    for list in res:
        sum1 = 0
        for i in range(len(list)):
            sum1 += (list[i] * (10 ** (len(list) - 1 - i)))
        resSum.append(sum1)
    print(sum(resSum))
