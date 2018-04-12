class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.sum = 0
        self.window = []
        self.max_size = size
        self.cur_size = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.cur_size < self.max_size:
            self.cur_size += 1
            self.window = self.window + [val]
            self.sum += val
        else:
            self.sum = self.sum - self.window[0] + val
            self.window = self.window[1:] + [val]
        
        return float(self.sum) / float(self.cur_size)
   

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)