class MyQueue(object):
    
    def __init__(self):
        self.list_queue = []
    
    def dequeue(self):
        return self.list_queue.pop(0)
        
    def enqueue(self, x):
        self.list_queue.append(x) 
    
    def front(self):
        return self.list_queue[0]
    
    def size(self):
        return len(self.list_queue)
    
    def is_empty(self):
        return self.size() == 0


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = MyQueue()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.enqueue(x)
        for i in xrange(0, self.queue.size()-1):
            self.queue.enqueue(self.queue.dequeue())
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty(): return 0        
        return self.queue.dequeue()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty(): return 0
        return self.queue.front()
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue.is_empty()
        

