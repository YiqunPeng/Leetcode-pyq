class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        
        dp = [sys.maxsize] * (n+1)
        
        dp[0], dp[1] = 0, 0
        
        for i in range(2, n+1):
            for j in range(1, i//2+1):
                if (i-j) % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i-j) // j + 1)
        
        return dp[n]