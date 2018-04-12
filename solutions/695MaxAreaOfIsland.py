class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(x, y, n, m, grid):
            area = 1
            grid[x][y] = 0
            fx = [[x-1,y], [x+1,y], [x,y-1], [x,y+1]]
            for i in range(0,4):
                n_x, n_y = fx[i][0], fx[i][1]
                if n_x >= 0 and n_x < n and n_y >= 0 and n_y < m and grid[n_x][n_y] == 1:
                    area += dfs(n_x, n_y, n, m, grid)
            return area
        
        ans = 0
        n, m = len(grid), len(grid[0])
        
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == 1:
                    area = dfs(i, j, n, m, grid)
                    if area > ans:
                        ans = area
        
        return ans