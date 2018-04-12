class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        minutes = []
        pos_list = [i for i in xrange(10)]
        comb_list = list(itertools.combinations([i for i in xrange(10)], num))
        for comb in comb_list:
            minute = self.compute_minutes(comb)
            if minute >= 720:
                continue
            minutes.append(self.compute_minutes(comb))
        minutes.sort()
        for minute in minutes:
            ans.append(self.minutes_format(minute))
        return ans
    
    def compute_minutes(self, comb):
        # enum = [480, 240, 120, 60, 32, 16, 8, 4, 2, 1]
        enum = [1, 2, 4, 8, 16, 32, 60, 120, 240, 480]
        low_dig = 0
        minutes = 0
        for c in comb:
            if c >= 0 and c <= 5:
                low_dig += enum[c]
            minutes += enum[c]
        if low_dig >= 60:
            return 1000
        return minutes
    
    def minutes_format(self, m):
        hour = m / 60
        minute_10 = m % 60 / 10
        minute_1 = m % 60 % 10
        return str(hour) + ':' + str(minute_10) + str(minute_1)