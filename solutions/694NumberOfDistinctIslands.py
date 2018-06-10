class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        
        island_list = set()
        m, n = len(grid), len(grid[0])
        v = [[False for j in range(n)] for i in range(m)]
        
        def bfs(x, y, v):
            island = []
            m, n = len(grid), len(grid[0])
            q = [(x, y)]
            while q:
                i, j = q.pop(0)
                for n_i, n_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if not (0 <= n_i < m and 0 <= n_j < n) or v[n_i][n_j]:
                        continue
                    if grid[n_i][n_j] == 1:
                        v[n_i][n_j] = True
                        island.append((n_i - x, n_j - y))
                        q.append((n_i, n_j))
            return str(island)
        

        for i in range(m):
            for j in range(n):
                if v[i][j]: continue
                if grid[i][j] == 1 and not v[i][j]:
                    v[i][j] = True
                    island_list.add(bfs(i, j, v))
        
        return len(island_list)
        