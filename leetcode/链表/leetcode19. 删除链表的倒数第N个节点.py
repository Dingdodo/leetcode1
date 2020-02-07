# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or n<=0:
            return head
        # 头结点
        dummyHead=ListNode(0)
        dummyHead.next=head

        p=dummyHead
        q=dummyHead
        k=0
        while q.next:
           #  增加了头结点所以k多了=n
           if k<n:
               q=q.next
               k+=1
               continue
           p=p.next
           q=q.next
        p.next=p.next.next

        return dummyHead.next
