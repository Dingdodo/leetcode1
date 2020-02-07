class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next

        return self.head

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        p=head
        q=head.next

        while p.next and q.next:
            pass








if __name__ == '__main__':
    s=Solution()
    data=[2,1,4,5,6]
    s.initList(data)
    import numpy as np
    arr=[[0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [1, 0, 1, 0]],


