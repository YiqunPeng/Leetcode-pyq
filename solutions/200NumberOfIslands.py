class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """ 
        if not grid: return 0
        
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]
        
        def dfs(x, y):
            visited[x][y] = True  
            for n_x, n_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if not (0 <= n_x < len(grid) and 0 <= n_y < len(grid[0])):
                    continue
                if grid[n_x][n_y] == '1' and not visited[n_x][n_y]:
                    dfs(n_x, n_y)
            
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    ans += 1
                    dfs(i, j)
                    
        return ans