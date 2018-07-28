class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        
        for i in range(len(s)):
            if s[i] == 'A':
                a += 1
                if a > 1: return False
            if 0 < i < len(s)-1:
                if s[i-1] == s[i] == s[i+1] == 'L':
                    return False
        
        return True