class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        def hight(root):
            if not root:
                return 0
            nleft=1+hight(root.left)
            nrignt=1+hight(root.right)
            return max(nleft,nrignt)
        if abs(hight(root.left),hight(root.right))>1:
            return False
        return self.isBalanced(root.left)and self.isBalanced(root.right)
if __name__ == '__main__':
    nums=[3,9,20,None,None,15,7]


    t=TreeNode(nums[0])
