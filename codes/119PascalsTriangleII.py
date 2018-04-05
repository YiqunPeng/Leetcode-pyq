class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1]
        for i in xrange(1, rowIndex + 1):
            ans.append(self.count(rowIndex, i))
        return ans
    
    def count(self, m, n):
        res = 1
        if (m - n) > n:
            for i in xrange(m-n+1, m+1):
                res *= i
            for i in xrange(1, n+1):
                res /= i
        else:
            for i in xrange(n+1, m+1):
                res *= i
            for i in xrange(1, m-n+1):
                res /= i
        return res