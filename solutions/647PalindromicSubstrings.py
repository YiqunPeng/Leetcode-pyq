class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)      
        dp = [[0] * s_len for i in range(s_len)]
        
        ans = 0
        
        for i in range(1, s_len):
            for j in range(i):
                if s[i] == s[j]:
                    if i - j <= 2 or dp[j+1][i-1] == 1:
                        ans += 1
                        dp[j][i] = 1
                        dp[j+1][i-1] = 1
                    if dp[j+1][i-1] == -1:
                        dp[j][i] = -1
                else:
                    dp[j][i] = -1
        
        return ans + s_len        