# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        def overlap(i1, i2):
            if i1.start >= i2.end or i2.start >= i1.end:
                return False
            else:
                return True
            
        
        length = len(intervals)
        
        sorted_intervals = sorted(intervals, key=lambda x:x.start)
        
        for i in range(length-1):
            if overlap(sorted_intervals[i], sorted_intervals[i+1]):
                return False
        
        return True