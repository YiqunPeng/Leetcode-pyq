class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.min is None or x <= self.min:      
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        if self.stack.pop() == self.min:
            self.min = self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()