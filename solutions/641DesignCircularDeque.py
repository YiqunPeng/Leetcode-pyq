class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.deque = [-1] * k
        self.front = 0
        self.rear = 0
        self.k = k
        self.size = 0
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull(): return False
        
        self.deque[self.front] = value
        self.front = (self.front - 1) % self.k
        self.size += 1
        if self.size == 1: self.rear = (self.rear + 1) % self.k
 
        return True
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull(): return False
        
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        if self.size == 1: self.front = (self.front - 1) % self.k
 
        return True
        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty(): return False
        
        self.front = (self.front + 1) % self.k
        self.size -= 1
        
        if self.isEmpty(): self.rear = (self.rear - 1) % self.k

        return True
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty(): return False
        
        self.rear = (self.rear - 1) % self.k
        self.size -= 1
        
        if self.isEmpty(): self.front = (self.front + 1) % self.k
 
        return True
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self.deque[(self.front + 1) % self.k]
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self.deque[(self.rear - 1) % self.k]
        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.size == 0
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()