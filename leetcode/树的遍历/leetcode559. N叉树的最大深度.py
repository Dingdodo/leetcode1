class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if len(root.children)==0:
            return 1
        # 队列
        que=[]
        que.append(root)
        depth=0
        while que:
            count=len(que)
            depth+=1
            while count:
                curNode=que.pop()
                if curNode.children:
                    for tmp in curNode.children:
                        que.append(tmp)
                count-=1
        return depth
# 方法2
def maxDepth2(self, root: 'Node') -> int:

    def height(root):
        if not root:
           return 0
        depth=0
        for i in root.children:
            depth=max(height(i),depth)
        return 1+depth
    return height(root)


