# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next :
            return head
        # 设置空结点
        d = ListNode(0)
        d.next = head
        head = d
        p = head
        q = p.next

        while q:
            num=0
            while q and p.next.val==q.val:
                q=q.next
                num+=1
            if num>1:
                p.next=q
            else:
                p=p.next
        return head.next

