# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals_len = len(intervals)
        if intervals_len <= 1: return 0
        
        intervals = sorted(intervals, key=lambda i: i.start)
        
        ans = 0
        
        left, right = 0, 1
        while left < right and right < intervals_len:
            if intervals[left].end <= intervals[right].start:
                left = right
                right += 1
            else:
                ans += 1
                if intervals[left].end > intervals[right].end:
                    left = right
                    right += 1
                else:
                    right += 1
        
        return ans
        
    
        
        
