class Solution:
    # dp
    # time: O(len(s) * len(p))
    # space: O(len(s) * len(p))
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        alpha = set([chr(ord('a')+i) for i in range(26)])
        
        s_len, p_len = len(s), len(p)
        dp = [[False for j in range(p_len+1)] for i in range(s_len+1)]
        dp[0][0] = True
        
        for i in range(p_len):
            dp[0][i+1] = p[i] == '*' and dp[0][i-1]
        
        for i in range(s_len):
            for j in range(p_len):
                if p[j] == '.' or (p[j] in alpha and p[j] == s[i]):
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    if p[j-1] == '.' or p[j-1] == s[i]:
                        dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j] or dp[i+1][j-1]
                    else:
                        dp[i+1][j+1] = dp[i+1][j-1]

        return dp[-1][-1]