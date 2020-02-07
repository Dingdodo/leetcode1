class LNode(object):
    #结点初始化函数, p 即模拟所存放的下一个结点的地址
    #为了方便传参, 设置 p 的默认值为 0
    def __init__(self, data, p=0):
        self.data = data
        self.next = p

class LinkList(object):
    def __init__(self):
       self.head=None

    #链表初始化函数, 方法类似于尾插
    def initList(self, data):
        #创建头结点
        self.head = LNode(data[0])
        p = self.head
        #逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = LNode(i)
            p.next = node
            p = p.next
        return self.head

    # 从尾到头打印链表
    def printH(self,p:LNode):
        
        ans_stack=[]
        while p:
            print(p.data)
            ans_stack.append(p)
            p=p.next
        return ans_stack
    # 递归 本质就是一个栈
    def PListRev(self,p:LNode):
        if p:
            if p.next:
                self.PListRev(p.next)
            print(p.data)




if __name__ == '__main__':
    l=LinkList()
    data=[1,2,3,4,5,6]
    p=l.initList(data)
    ans=l.printH(p)
    while ans:
        pdata=ans.pop()
        print(pdata.data)
    print("=========================")
    l.PListRev(p)
