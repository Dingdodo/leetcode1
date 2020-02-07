# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root or L>R:
            return
        stack=[]
        res=[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            curNode=stack.pop()
            res.append(curNode.val)
            root=curNode.right
        n=len(res)
        sum1=0
        for i in range(n):
            if res[i]>=L and res[i]<=R:
                sum1+=res[i]

        return sum1
    # 方法2
    def rangeSumBST1(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node, L, R):
            val = node.val
            if val >= L and val <= R:
                self.ans += val
            if L < val and node.left:
                dfs(node.left, L, R)
            if R > val and node.right:
                dfs(node.right, L, R)
        if root is None:
            return 0
        self.ans = 0
        dfs(root, L, R)
        return self.ans





