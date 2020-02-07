# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not (head or head.next):
            return head
        low,fast=head,head
        while fast and fast.next:
            low=low.next
            fast=fast.next.next
        return low
