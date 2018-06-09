class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return k
        if n == 2: return k * k
        
        dp = [[0 for j in range(k)] for i in range(n)]
        for i in range(k):
            dp[0][i] = 1
            dp[1][i] = k
        dp_sum = [0] * n
        dp_sum[0] = k
        dp_sum[1] = k * k
        
        for i in range(2, n):
            for j in range(k):
                dp[i][j] = dp_sum[i-1] - dp[i-1][j] + dp_sum[i-2] - dp[i-2][j]
            dp_sum[i] = sum(dp[i])
        
        return dp_sum[-1]
