from bisect import insort_left

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.count = 0
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        insort_left(self.nums, num)
        self.count += 1
        

    def findMedian(self):
        """
        :rtype: float
        """
        if self.count % 2 == 1:
            return self.nums[self.count//2] / 1.
        else:
            return (self.nums[self.count//2-1]+self.nums[self.count//2]) / 2.
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()