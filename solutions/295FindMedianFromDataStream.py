# max heap + min heap
# addNum -- time: O(logn)
# findMedian -- time: O(1)
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        
        if len(self.small) > len(self.large):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.
        else:
            return self.large[0] / 1.


# binary search
# addNum -- time: O(n)
# findMedian -- time: O(1)
# from bisect import insort_left

# class MedianFinder:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.nums = []
#         self.count = 0
        

#     def addNum(self, num):
#         """
#         :type num: int
#         :rtype: void
#         """
#         insort_left(self.nums, num)
#         self.count += 1
        

#     def findMedian(self):
#         """
#         :rtype: float
#         """
#         if self.count % 2 == 1:
#             return self.nums[self.count//2] / 1.
#         else:
#             return (self.nums[self.count//2-1]+self.nums[self.count//2]) / 2.
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()