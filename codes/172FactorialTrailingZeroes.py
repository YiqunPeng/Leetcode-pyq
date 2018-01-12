class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        cnt = 5
        
        while cnt <= n:
            ans += (n // cnt)
            cnt *= 5
            
        return ans