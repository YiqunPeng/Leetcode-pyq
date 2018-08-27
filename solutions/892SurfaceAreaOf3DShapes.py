class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                
                ans = ans + 6 * grid[i][j] - 2 * (grid[i][j] - 1)
                
                for neighbor in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if not (0 <= neighbor[0] < m and 0 <= neighbor[1] < n):
                        continue
                    ans = ans - min(grid[i][j], grid[neighbor[0]][neighbor[1]])
    
        return ans