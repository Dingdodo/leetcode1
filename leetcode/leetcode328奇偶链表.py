# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    # 链表初始化函数, 方法类似于尾插

    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node

            p = p.next

        return self.head

    def oddEvenList(self, head: ListNode) -> ListNode:
      if not head or not head.next:
          return head
      # 奇数头节点
      p=head
      # 偶数头节点
      q=head.next
      t=q
      while q.next and p.next:
          p.next=q.next
          p=q.next

          q.next=p.next
          q=p.next

      p.next=t
      return head

    def printList(self, head: ListNode) -> ListNode:
          if head:
              while head:
                  print(head.val)
                  head=head.next

if __name__ == '__main__':
   s=Solution()
   data=[1,2,3,4,5,6,7,8]

   head=s.initList(data)
   p=s.oddEvenList(head)

   s.printList(p)


