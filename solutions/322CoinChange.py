class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for c in coins:
            if c < len(dp):
                dp[c] = 1
        
        for i in range(len(dp)):
            for c in coins:
                if i - c > 0:
                    dp[i] = min(dp[i], dp[i-c]+1)
        
        return dp[-1] if dp[-1] != sys.maxsize else -1
