# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow,fast=head,head
        prev=None
        while fast:
            slow=slow.next
            if fast.next:
                fast=fast.next.next
            else:
                fast=fast.next
        while slow:
            ovn=slow.next
            slow.next=prev
            prev=slow
            slow=ovn
        while head and prev:
            if head.val!=prev.val:
                return False
            head=head.next
            prev=prev.next
        return True


















