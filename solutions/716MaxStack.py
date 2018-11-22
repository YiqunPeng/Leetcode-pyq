class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max = None
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.max is None or self.max <= x:
            self.stack.append(self.max)
            self.max = x
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        res = self.stack.pop() 
        if res == self.max:
            self.max = self.stack.pop()
        return res
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
    

    def peekMax(self):
        """
        :rtype: int
        """
        return self.max
        

    def popMax(self):
        """
        :rtype: int
        """
        temp = []
        while self.top() != self.max:
            temp.append(self.pop())
            
        res = self.pop()
        
        while temp:
            self.push(temp.pop())
        
        return res
    

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()