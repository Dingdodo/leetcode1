# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        dummyHead=ListNode(-1)
        dummyHead.next=head
        pre=dummyHead
        for i in range(m):
            pre=pre.next
        head=pre.next

        for i in range(m,n):
            cur=head.next
            head.next=cur.next
            cur.next=pre.next
            pre.next=cur

        return dummyHead.next

