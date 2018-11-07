class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        
        dp = [[1] * 3 for i in range(4)]
        dp[3][0] = 0
        dp[3][2] = 0
        
        if N == 1:   
            return sum(map(sum, dp)) % mod
        
        
        for i in range(1, N):
            ndp = [[0] * 3 for i in range(4)]
            
            ndp[0][0] = dp[1][2] + dp[2][1]
            ndp[0][1] = dp[2][0] + dp[2][2]
            ndp[0][2] = dp[1][0] + dp[2][1]
            
            ndp[1][0] = dp[0][2] + dp[2][2] + dp[3][1]
            ndp[1][1] = 0
            ndp[1][2] = dp[0][0] + dp[2][0] + dp[3][1]
            
            ndp[2][0] = dp[0][1] + dp[1][2]
            ndp[2][1] = dp[0][0] + dp[0][2]
            ndp[2][2] = dp[0][1] + dp[1][0]
            
            ndp[3][1] = dp[1][0] + dp[1][2]
            
            dp = ndp
            
        return sum(map(sum, dp)) % mod