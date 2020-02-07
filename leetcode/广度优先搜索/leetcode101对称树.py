# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 方法一 递归
    def isSymmetric(self, root: TreeNode) -> bool:

        if root==None:
            return True
        return self.isMirror(root.left,root.right)

    # 递归函数
    def isMirror(self,left:TreeNode,right:TreeNode)->bool:
        # 传过来的左右子树都为空
        if left==None and right==None:
            return True
        # 一个为空一个不为空 返回false
        if (left==None and right!=None)or ((left!=None and right==None)):
            return False
        # 左右子树都不为空，值不相等 返回fasle
        if left.val!=right.val:
            return False
        # 左右子树值相等情况，左子树的左子树和右子树的右子树判断，左子树的右子树和右子树的左子树判断
        else:
            return self.isMirror(left.left,right.right)& self.isMirror(left.right,right.left)

        # 方法二  广度优先搜索（迭代）
    def isSymmetric1(self, root: TreeNode) -> bool:
            # 定义栈
            sta=[]
            # 进 两次根节点
            sta.append(root)
            sta.append(root)
            while len(sta)!=0:
                s1=sta.pop()
                s2=sta.pop()
                # True or True continue

                if not s1 and not s2:
                    continue
                elif s1==None or s2==None:
                    return False
                else:
                    if s1.val!=s2.val:
                        return False
                    else:
                        sta.append(s1.left)
                        sta.append(s2.right)
                        sta.append(s1.right)
                        sta.append(s2.left)
            return True






if __name__== "__main__":
    s=Solution()
    # root=[1,2,2,3,4,4,3]
    root=TreeNode(1)

    res=s.isSymmetric(root)
    print(res)