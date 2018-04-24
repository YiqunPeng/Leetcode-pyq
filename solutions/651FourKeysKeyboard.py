class Solution:
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0] * (N + 1)
        
        for i in range(1, N + 1):
            dp[i] = i
            for j in range(1, i - 2):
                dp[i] = max(dp[i], dp[j] * (i - 1 - j))
        
        return dp[N]
            