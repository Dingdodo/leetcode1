class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return
        # 增加哑结点方便
        dummpyHead1=ListNode(0)
        dummpyHead2=ListNode(0)
        # 连接小于x的一条链表
        p1=dummpyHead1
        # 链接大于x的一条链表
        p2=dummpyHead2
        while head:
            if head.val<x:
                p1.next=head
                head=head.next
                p1=p1.next
                p1.next=None
            else:
                p2.next=head
                head=head.next
                p2=p2.next
                p2.next=None
        p1.next=dummpyHead2.next
        return dummpyHead1.next

