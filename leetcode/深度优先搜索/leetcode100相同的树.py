class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 都是空
        if p==None and q==None:
            return True
        # 一个空一个非空
        if (p==None and q)or (p and q==None):
        # if not (p or q):
            return False
        #只有一个结点
        if p.left==p.right==None and q.left==q.right==None and p.val==q.val:
            return True

        #两个栈
        stackp=[]
        stackq=[]
        stackp.append(p)
        stackq.append(q)
        resp=[]
        resq=[]
        resp.append(p.val)
        resq.append(q.val)
        i=0
        while stackp and stackq:
            currp=stackp.pop()
            currq=stackq.pop()
            # p树 数组
            if currp.left:
                stackp.append(currp.left)
                resp.append(currp.left.val)
            else:
                resp.append(-1)

            if currp.right:
                stackp.append(currp.right)
                resp.append(currp.right.val)
            else:
                resp.append(-1)
            #q树 数组
            if currq.left:
                stackq.append(currq.left)
                resq.append(currq.left.val)
            else:
                resq.append(-1)

            if currq.right:
                stackq.append(currq.right)
                resq.append(currq.right.val)
            else:
                resq.append(-1)
            i+=1
        for j in range(i+1):
            if resq[j]!=resp[j]:
                return False
        return True






