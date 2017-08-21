class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list_stack = []
        self.min = sys.maxsize       

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.min >= x:
            self.list_stack.append(self.min)
            self.min = x
        self.list_stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        if self.list_stack.pop(-1) == self.min:
            self.min = self.list_stack.pop(-1)
        

    def top(self):
        """
        :rtype: int
        """
        return self.list_stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        