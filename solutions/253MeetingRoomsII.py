# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start.sort()
        end.sort()
        
        max_m, curr_m = 0, 0
        
        s_p, e_p = 0, 0
        while s_p < len(intervals):
            if start[s_p] < end[e_p]:
                curr_m += 1
                max_m = max(max_m, curr_m)
                s_p += 1
            elif start[s_p] > end[e_p]:
                curr_m -= 1
                e_p += 1
            else:
                s_p += 1
                e_p += 1
        
        return max_m
                
        