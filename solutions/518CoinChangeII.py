class Solution(object):
    # dp
    # time: O(n * m) n -- number of coins, m -- amount
    # space: O(m)
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            if c < amount + 1:
                dp[c] += 1
            for i in range(c + 1, amount + 1):
                dp[i] += dp[i - c]
        
        return dp[-1]

    # dp
    # time: O(n * m)
    # space: O(n * m)
    # def change(self, amount, coins):
    # """
    # :type amount: int
    # :type coins: List[int]
    # :rtype: int
    # """
    # dp = [[0 for j in range(amount+1)] for i in range(len(coins)+1)]
    # dp[0][0] = 1
    
    # for i in range(1, len(coins)+1):
    #     dp[i][0] = 1

    #     for j in range(1, amount+1):
    #         if j >= coins[i-1]:
    #             dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
    #         else:
    #             dp[i][j] = dp[i-1][j]
    
    # return dp[-1][-1]