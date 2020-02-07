from typing import List

ans = []
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        global ans
        if not root:
            return []
        self.dfs(root,sum,[])
        return ans


    # 递归函数
    def dfs(self,root:TreeNode,sum,res:List):
        sum-=root.val
        res.append(root.val)
        if not root.right and not root.left:
            ans.append(res)
            return
        if root.right:
            self.dfs(root.right,sum)
        if root.left:
            self.dfs(root.left,sum)

