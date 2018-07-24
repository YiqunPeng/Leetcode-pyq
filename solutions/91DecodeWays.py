class Solution:
    # dp 
    # time: O(n)
    # space: O(1)
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        dp = [0] * 2
        if s[0] != '0':
            dp[0] = 1
        else:
            return 0

        for i in range(1, n):
            dp_1 = dp[i%2]

            dp[i%2] = dp[(i-1)%2] if s[i] != '0' else 0

            if s[i-1] != '0' and 1 <= int(s[i-1:i+1]) <= 26:
                dp[i%2] += max(1, dp_1)

            if dp[i%2] == 0: return 0

        return dp[(len(s)-1)%2]
    
    
    # dp
    # time: O(n)
    # space: O(n)
    # def numDecodings(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     n = len(s)

    #     dp = [0] * n
    #     if s[0] != '0':
    #         dp[0] = 1
    #     else:
    #         return 0

    #     for i in range(1, n):
    #         dp[i] = dp[i-1] if s[i] != '0' else 0

    #         if s[i-1] != '0' and 1 <= int(s[i-1:i+1]) <= 26:
    #             if i == 1:
    #                 dp[i] += 1
    #             else:
    #                 dp[i] += dp[i-2]

    #         if dp[i] == 0: return 0

    #     return dp[-1]
        