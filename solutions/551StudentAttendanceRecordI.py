class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cnt_a = 0
        for c in s:
            if c == 'A':
                cnt_a += 1
            if cnt_a > 1:
                return False
        
        for i in xrange(1, len(s) - 1):
            if s[i] == 'L' and s[i-1] == 'L' and s[i+1] == 'L':
                return False
        
        return True