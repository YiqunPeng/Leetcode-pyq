class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0  
        m, n = len(grid), len(grid[0])
        
        dp = [0 for j in range(n)]
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = grid[0][j] + dp[j-1]
            
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        
        return dp[-1]