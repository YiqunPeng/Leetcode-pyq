class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: return s == ''
        if not s and p[0] != '*': return False
        
        s_len, p_len = len(s), len(p)
        dp = [[False for j in range(p_len+1)] for i in range(s_len+1)]
        
        dp[0][0] = True
        
        p_dic = [False] * p_len
        
        for i in range(p_len):
            if p[i] == '*':
                dp[0][i+1] = dp[0][i]
            else:
                break
        
        for i in range(1, s_len+1):
            for j in range(1, p_len+1):
                if p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                    p_dic[j-1] = p_dic[j-1] or dp[i][j]
                elif p[j-1] == '*':
                    if j == 1:
                        dp[i][j] = True
                        p_dic[0] = True
                    else:
                        dp[i][j] = p_dic[j-2]
                        p_dic[j-1] = p_dic[j-1] or dp[i][j]
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
                    p_dic[j-1] = p_dic[j-1] or dp[i][j]
        
        return dp[-1][-1]
