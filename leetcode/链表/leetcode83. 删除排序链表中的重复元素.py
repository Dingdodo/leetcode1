# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
           return head
        p=head
        q=head.next
        while p and q:
            if p.val==q.val:
                p.next=q.next
                q=q.next
            else:
                p=p.next
                q=q.next
        return head



