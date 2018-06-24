class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        dp = [0] * (n + 1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        else:
            return 0

        for i in range(2, n+1):
            dp[i] = dp[i-1] if s[i-1] != '0' else 0
            if s[i-2] != '0' and 1 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
            if dp[i] == 0: return 0

        return dp[-1]
        