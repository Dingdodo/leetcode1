class MyQueue:
    #  两个栈
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack=[]
        self.outStack=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inStack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        输出栈先空才能进栈
        """
        if len(self.outStack)==0:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.outStack)==0:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.outStack and not self.inStack