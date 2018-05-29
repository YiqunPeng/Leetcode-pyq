class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid: return 0
        
        grid = obstacleGrid
        m, n = len(grid), len(grid[0])
        
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1 if grid[0][0] == 0 else 0
        for i in range(1, m):
            if grid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]
        for j in range(1, n):
            if grid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j-1]
        
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]