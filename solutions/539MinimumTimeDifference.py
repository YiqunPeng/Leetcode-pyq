class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def time2minutes(timePoint):
            hour = int(timePoint[0]) * 10 + int(timePoint[1])
            minute = int(timePoint[3]) * 10 + int(timePoint[4])
            return hour * 60 + minute
        
        minutes = []
        for timePoint in timePoints:
            minute = time2minutes(timePoint)
            minutes.append(minute)
            minutes.append(minute+1440)
        minutes.sort()
        diff = []
        for i in xrange(0, len(minutes)-1):
            diff.append(minutes[i+1] - minutes[i])
        print(minutes)
        print(diff)
        return min(diff)
        