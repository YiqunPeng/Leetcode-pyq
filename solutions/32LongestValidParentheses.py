class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        
        ans = 0
        
        n = len(s)
        dp = [0] * n
        
        stack = []
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
                dp[i] = 0
            else:
                if not stack:
                    dp[i] = 0
                else:
                    pos = stack.pop()
                    dp[i] = dp[pos-1] + i - pos + 1
                    ans = max(ans, dp[i])
        
        return ans               