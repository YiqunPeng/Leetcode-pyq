class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []
        self.b = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.a.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.b:
        #     return self.b.pop()
        # else:
            while self.a:
                self.b.append(self.a.pop())
        return self.b.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())
        return self.b[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.b) + len(self.a) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()