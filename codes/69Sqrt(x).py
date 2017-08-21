class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        
        ans = 1
        
        while ans != (ans + x / ans) / 2:
            ans = (ans + x / ans) / 2
            if ans ** 2 <= x and (ans+1) ** 2 > x:
                return ans
        
        return ans