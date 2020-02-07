class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
# merge(l1, l2)，双路归并，我相信这个操作大家已经非常熟练的，就不做介绍了。
# cut(l, n)，可能有些同学没有听说过，它其实就是一种 split 操作，即断链操作。不过我感觉使用 cut 更准确一些，它表示，将链表 l 切掉前 n 个节点，并返回后半部分的链表头。
# 额外再补充一个 dummyHead 大法，已经讲过无数次了，仔细体会吧。
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return
        dummpyHead=ListNode(0)
        dummpyHead.next=head
        p=head
        n=0
        while p:
            n+=1
            p=p.next
        index = []
        for i in range(n):
            if 2**i>n:
                break
            else:
                index.append(2**i)
        for i in index:
            curNode=dummpyHead.next
            tail=dummpyHead
            while curNode:
                left=curNode
                right=self.cut(left,i)
                curNode=self.cut(right,i)

                tail.next=self.merge(left,right)
                while tail.next:
                    tail=tail.next
        return dummpyHead.next

    def cut(self,head: ListNode,n:int) -> ListNode:
        p=head

        while p and n-1:
            p=p.next
            n-=1
        if not p:
            return None
        q=p.next
        p.next=None
        return q

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
         dummyHead=ListNode(-1)
         p=dummyHead
         while(l1 and l2):
             if l1.val<l2.val:
                 p.next=l1
                 p=l1
                 l1=l1.next
             else:
                 p.next=l2
                 p=l2
                 l2=l2.next
         if l1:
             p.next=l1
         if l2:
             p.next=l2
         return dummyHead.next


    # 方法2
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        List = []
        while head:
            List.append(head.val)
            head = head.next
        List.sort()

        ans = tmp = ListNode(-1)

        for i in List:
            tmp.next = ListNode(i)
            tmp = tmp.next

        return ans.next



if __name__ == '__main__':
   p1=ListNode(1)
   p2=ListNode(2)
   p3=ListNode(3)
   p1.next=p2
   s=Solution()
   q=s.merge(p1,p3)
   while q:
       print(q.val)
       q=q.next


