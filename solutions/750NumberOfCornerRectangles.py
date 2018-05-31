class Solution:
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        dp = [[0 for j in range(n)] for i in range(n)]
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: 
                    continue
                
                for k in range(j+1, n):
                    if grid[i][k] == 1:
                        ans += dp[j][k]
                        dp[j][k] += 1
        
        return ans
        
        