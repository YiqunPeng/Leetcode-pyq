# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        schedules = []
        for s in schedule:
            schedules = schedules + s
        schedules = sorted(schedules, key=lambda s: s.start)

        left, right = 0, 1
        while right < len(schedules):
            if schedules[left].end < schedules[right].start:
                left = right
                right += 1
            else:
                schedules[left].end = max(schedules[left].end, schedules[right].end)
                schedules.pop(right)
                
        ans = []
        for i in range(1, len(schedules)):
            interval = Interval(schedules[i-1].end, schedules[i].start)
            ans.append(interval)
        return ans
                        