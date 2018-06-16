# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        
        intervals = sorted(intervals, key=lambda i: i.start)
        length = len(intervals)
        if length <= 1: return intervals
        
        left, right = 0, 1
        while right < length:
            if intervals[left].end < intervals[right].start:
                ans.append(intervals[left])
                left = right
                right += 1
            else:
                intervals[left].end = max(intervals[left].end, intervals[right].end)
                right += 1
                
        ans.append(intervals[left])
        return ans