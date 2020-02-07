# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        p=head
        q=head
        while p.next and p.val!=None:
            p.val=None
            p=p.next

        if not p.next:
            return
        if p.val==None:
            i=0
            while p!=q:
               q=q.next
               i+=1
            return i
        return
    # 快慢指针
    def detectCycle1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        low =head
        fast=head
        q=head
        while fast and fast.next:
            fast=fast.next.next
            low=low.next
            if low==fast:
                break
        if low==fast and fast and fast.next:
           while q!=low:
               low=low.next
               q=q.next

           return q
        return




