# Definition for a binary tree node.
#
"""
首先寻找根节点相同节点。
先判断根节点是否相等，如果相等，再判断子树是否相等。
否则，判断子树是否等于原树左子树的子树。
否则，判断子树是否等于原树右子树的子树。

然后判断子树是否相等
如果都为空，则相等。
如果其中一个不为空，则不等。
如果都不为空，但值不相等，则不等。
递归判断对应左右节点是否相等。
"""


#
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # DoesTreeHavaTree
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        result=False

        if s and t:
            if s.val==t.val:
                result=self.DoesTreeHavaTree(s,t)
            if not result:
                print(t.val)
                result=self.isSubtree(s.left,t)
            if not result:
                result=self.isSubtree(s.right,t)

        return result


    def DoesTreeHavaTree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not (t or s):
        # if (not t and s)or (t and not s):
            return False
        if t.val!=s.val:
            return False
        return self.DoesTreeHavaTree(s.left,t.left) and self.DoesTreeHavaTree(s.right,t.right)
if __name__ == '__main__':
    sd=Solution()

    t = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t1 = TreeNode(1)
    t2 = TreeNode(2)

    t.left=t4
    t.right=t5
    t4.left=t1
    t4.right=t2

    s = TreeNode(4)
    s1 = TreeNode(1)
    s2 = TreeNode(2)

    s.left=s1
    s.right=s2
    print(sd.isSubtree(t,s))