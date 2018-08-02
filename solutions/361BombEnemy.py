class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        
        ans = 0
        m, n = len(grid), len(grid[0])
        row_hit, col_hit = 0, [0] * n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W': continue
                
                if not j or grid[i][j-1] == 'W':
                    row_hit = 0
                    for k in range(j, n):
                        if grid[i][k] == 'E': row_hit += 1
                        if grid[i][k] == 'W': break
                
                if not i or grid[i-1][j] == 'W':
                    col_hit[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'E': col_hit[j] += 1
                        if grid[k][j] == 'W': break
                
                if grid[i][j] == '0': ans = max(ans, row_hit + col_hit[j])
        
        return ans
