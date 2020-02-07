# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head :
            return head
        if not head.next and head.val==val:
            return head
        d=ListNode(0)
        d.next=head
        head=d
        p=head
        q=head.next
        while q:
            if q.val!=val:
                q=q.next
                p=p.next
            else:
                p.next=q.next
                q=q.next
        return head.next



