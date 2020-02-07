# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        p=head
        import sys
        while p.next and p.val!=sys.maxint:
            p.val=sys.maxint
            p=p.next
        if not p.next:
            return False
        return True
    def hasCycle1(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        low=head
        fast=head
        while fast.next and fast:
            fast = fast.next.next
            low=low.next
            if fast==low:
                return True
        return False
