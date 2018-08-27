class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not t: return 1
        if not s: return 0
        
        s_len, t_len = len(s), len(t)
        
        dp = [[0] * s_len for i in range(t_len)]
        if s[0] == t[0]: dp[0][0] = 1 
        for j in range(1, s_len):
            if s[j] == t[0]:
                dp[0][j] = dp[0][j-1] + 1
            else:
                dp[0][j] = dp[0][j-1]
        
        for i in range(1, t_len):
            for j in range(i, s_len):
                if s[j] == t[i]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        
        return dp[-1][-1]