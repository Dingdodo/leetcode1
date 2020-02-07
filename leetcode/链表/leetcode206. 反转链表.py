# Definition for singly-linked list.
from Cython.Utility.MemoryView import free


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        r=None
        while head:
            p=head.next
            head.next=r
            r=head
            head=p
        return r
    def reverseList1(self, head: ListNode) -> ListNode:
      if not head:
          return
      dummyHead=ListNode(-1)
      dummyHead.next=head
      pre=dummyHead
      p=head.next
      head.next=None
      while p:
          q=p.next
          pre.next=p
          p.next=pre.next
          p=q
      # free(dummyHead)
      return head