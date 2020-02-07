from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not (inorder or postorder):
            return
        x=postorder[-1]
        root=TreeNode(x)
        i=inorder.index(x)
        root.left=self.buildTree(inorder[:i],postorder[:i])
        root.right=self.buildTree(inorder[i+1:],postorder[i:-1])
        return root
    # 方法2
    def buildTree2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        postorder.reverse()
        index = 0

        def recursion(left=0, right=len(inorder)):
            nonlocal index
            if left == right:
                # print('kkk',index)
                return None
            root_val = postorder[index]
            root = TreeNode(root_val)
            k = index_map[root_val]
            index += 1
            # print(index, root_val)
            root.right = recursion(left=k + 1, right=right)

            root.left = recursion(left, right=k)

            return root

        index_map = {element: index for index, element in enumerate(inorder)}
        return recursion()
    # 方法3
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        #  assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
        assert (len(inorder) == len(postorder))
        self.numToIndex = dict()
        for i, num in enumerate(inorder):
            self.numToIndex[num] = i
        size = len(inorder)
        return self.buildTreeRecursive(inorder, 0, size - 1, postorder, 0, size - 1)

    def buildTreeRecursive(self, inorder, x1, y1, postorder, x2, y2):
        if x1 > y1:
            return None
        rootVal = postorder[y2]
        root = TreeNode(rootVal)
        index = self.numToIndex[rootVal]
        root.left = self.buildTreeRecursive(inorder, x1, index - 1, postorder, x2, x2 + index - x1 - 1)
        root.right = self.buildTreeRecursive(inorder, index + 1, y1, postorder, x2 + index - x1, y2 - 1)
        return root