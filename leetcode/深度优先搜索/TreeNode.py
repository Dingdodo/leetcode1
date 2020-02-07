# -*- coding: utf-8 -*-
class TreeNode:

    def __init__(self,value):

        self.value=value

        self.left=None

        self.right=None


class Tree_Method:

    def tree_Create(self, arr):

        '''

        利用二叉树的三个组成部分：根节点-左子树-右子树；传入的arr是一个多维列表，每一

        维最大为3，每一维中的内容依次表示根节点-左子树-右子树。然后递归的进行构建

        '''

        length = len(arr)  # 计算每一维的大小


        root = TreeNode(arr[0])  # 获取每一维的根节点

        if length >= 2:  # 判断是否有左子树

            root.left = self.tree_Create(arr[1])

        if length >= 3:  # 判断是否有右子树

            root.right = self.tree_Create(arr[2])

        return root

    def pre_Order(self, root):

        '''前序遍历，遵循根左右的顺序'''

        if root == None:
            return

        print(root.value, end=' ')

        self.pre_Order(root.left)

        self.pre_Order(root.right)

    def mid_Order(self, root):

        '''中序遍历，遵循左根右的顺序'''

        if root == None:
            return

        self.mid_Order(root.left)

        print(root.value, end=' ')

        self.mid_Order(root.right)

    def back_Order(self, root):

        '''遵循左右根的顺序'''

        if root == None:
            return

        self.back_Order(root.left)

        self.back_Order(root.right)

        print(root.value, end=' ')

    def BFS(self, root):

        '''

        广度优先遍历，即从上到下，从左到右遍历

        主要利用队列先进先出的特性，入队的时候

        是按根左右的顺序，那么只要按照这个顺序出队就可以了

        '''

        if root == None:
            return

        queue = []

        queue.append(root)  # 这儿用一个列表模仿入队

        while queue:

            current_node = queue.pop(0)  # 将队首元素出队

            print(current_node.value, end=' ')

            if current_node.left:  # 判断该节点是否有左孩子

                queue.append(current_node.left)

            if current_node.right:  # 判断该节点是否有右孩子

                queue.append(current_node.right)

    def DFS(self, root):#栈

        '''

        深度优先遍历，即先访问根结点，然后遍历左子树接着是遍历右子树

        主要利用栈的特点，先将右子树压栈，再将左子树压栈，这样左子树

        就位于栈顶，可以保证结点的左子树先与右子树被遍历

        '''

        if root == None:
            return

        stack = []

        stack.append(root)  # 这儿用一个列表模仿入队

        while stack:

            current_node = stack.pop()  # 将栈顶元素出栈

            print(current_node.value, end=' ')

            if current_node.right:  # 判断该节点是否有右孩子，有就入栈

                stack.append(current_node.right)

            if current_node.left:  # 判断该节点是否有左孩子，有就入栈。两个判断的顺序不能乱

                stack.append(current_node.left)


if __name__ == "__main__":
    arr = [2, [3, [4], [5]], [2, [4, [7]], [3]]]

    op = Tree_Method()

    tree = op.tree_Create(arr)

    print('前序遍历:', end='')

    op.pre_Order(tree)

    print()

    print('中序遍历:', end='')

    op.mid_Order(tree)

    print()

    print('后序遍历:', end='')

    op.back_Order(tree)

    print()

    print('广度优先遍历:', end='')

    op.BFS(tree)

    print()

    print('深度优先遍历:', end='')

    op.DFS(tree)
