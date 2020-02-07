class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    res = []
    num = []
    def maxPathSum(self, root: TreeNode) -> int:
        def helper2(root):
            stack = []
            while root or stack:
                while root:
                    stack.append(root)
                    root = root.left
                cur_node = stack.pop()
                self.helper(cur_node)
                self.num.append(self.res)
                self.res=[]
                root = cur_node.right
        helper2(root)
        maxS=-1<<32
        for list in self.num:
            if sum(list)>maxS:
               maxS=sum(list)
        return maxS
    # 先序遍历
    def helper(self,root):
            if not root:
                return
            self.res.append(root.val)
            self.helper(root.left)
            self.helper(root.right)
    # 方法2
    def maxPathSum2(self, root: TreeNode) -> int:
        #  self.res=float('-inf')
        self.res = -1<< 32

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            self.res = max(left + right + root.val, self.res)
            return max(0, max(left, right) + root.val)

        helper(root)
        return self.res



if __name__ == '__main__':
     pass