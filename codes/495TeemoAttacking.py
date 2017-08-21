class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries: return 0
        ans = 0
        
        for i in xrange(len(timeSeries)-1):
            if timeSeries[i+1] - timeSeries[i] >= duration:
                ans += duration
            else:
                ans += (timeSeries[i+1] - timeSeries[i])
                
        return ans + duration
        