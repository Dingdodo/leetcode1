class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not (head or head.next):
            return head
        left=head
        mid=self.midP(head)
        right=mid.next
        mid.next=None
        # 后链表需要反转
        right=self.reverse(right)
        # 合并
        self.merge(left,right)

    def midP(self,head:ListNode):
        low,fast=head,head
        while fast and fast.next:
            low=low.next
            fast=fast.next.next
        return low
    def reverse(self,head:ListNode):
        p=head
        r=None
        while p:
            q = p.next
            p.next = r
            r= head
            p= q
        return r

    def merge(self,left:ListNode,right:ListNode):

        while left.next and right:
            leftTemp=left.next
            rightTemp=right.next

            left.next=right
            right.next=leftTemp

            left=leftTemp
            right=rightTemp
















if __name__ == '__main__':
    p1=ListNode(1)
    p2=ListNode(2)
    p3=ListNode(3)
    p4=ListNode(4)
    p1.next=p2
    p2.next=p3
    p3.next=p4
    s=Solution()
    q=s.reorderList(p1)
    print(q.val)
