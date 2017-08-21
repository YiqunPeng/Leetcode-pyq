class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        if n == 1: return s
        
        for i in xrange(1, n):
            temp = ''
            cnt = 1
            c = s[0]
            for j in xrange(1, len(s)):
                if s[j] == c:
                    cnt += 1
                else:
                    temp = temp + str(cnt) + c
                    cnt = 1
                    c = s[j]
            s = temp + str(cnt) + c
        
        return s