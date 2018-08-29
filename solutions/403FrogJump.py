class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] != 1: return False
        
        n = len(stones)
        
        pos = {}
        for i, s in enumerate(stones):
            pos[s] = i
        
        dp = [[False] * n for i in range(n)]
        dp[1][1] = True
        
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                if dp[i][j]:
                    if j - 1 > 0 and stones[i] + j - 1 in pos: dp[pos[stones[i]+j-1]][j-1] = True
                    if stones[i] + j in pos: dp[pos[stones[i]+j]][j] = True
                    if stones[i] + j + 1 in pos: dp[pos[stones[i]+j+1]][j+1] = True
        
        return any(dp[-1][k] for k in range(n))