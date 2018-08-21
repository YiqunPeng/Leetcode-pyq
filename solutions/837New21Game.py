class Solution(object):
    # dp
    # time: O(n)
    # space: O(n)
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0 or N > K + W: return 1.
        
        dp = [0.] * (N + 1)
        dp[0] = 1.
        
        s = 1.
        
        for i in range(1, N + 1):
            dp[i] = s / W
            
            if i < K: s += dp[i]
            if i >= W: s -= dp[i - W]

        return sum(dp[K:])
