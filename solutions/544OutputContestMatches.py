class Solution:
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        def recursion(ans, val, sum, n):
            if sum > n + 1:
                ans = ans + str(val)
                return ans
            
            ans = ans + '(' \
                      + recursion(ans, val, sum*2-1, n) \
                      + ',' \
                      + recursion(ans, sum-val, sum*2-1, n) \
                      + ')'
            
            return ans
   

        return recursion('', 1, 3, n)
        