class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
       if not head:
           return
       dummpyHead=ListNode(0)
       dummpyHead.next=head
       p=head
       pre=dummpyHead
       while p:
           q=p.next
           while pre.next and p.val>pre.next.val:
               pre=pre.next
           p.next=pre.next
           pre.next=p
           p=q
           pre=dummpyHead
       return dummpyHead.next



