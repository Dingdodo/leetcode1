class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Queue=[]


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.Queue.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        i=len(self.Queue)
        while i>1:
            self.Queue.append(self.Queue.pop())
            i-=1
        return self.Queue.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        i = len(self.Queue)
        while i>1:
            self.Queue.append(self.Queue.pop())
            i-=1
        res=self.Queue[0]
        self.Queue.append(self.Queue.pop())

        return res


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.Queue
