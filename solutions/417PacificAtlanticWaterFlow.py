class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(i, j, h, flag, m, n): 
            flag[i][j] = True
            
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and not flag[ni][nj]:
                    if matrix[ni][nj] >= matrix[i][j]:
                        dfs(ni, nj, matrix[ni][nj], flag, m, n)
        
        
        if not matrix or not matrix[0]: return []
        
        m, n = len(matrix), len(matrix[0])
        p = [[False] * n for i in range(m)]
        a = [[False] * n for i in range(m)]
        
        for j in range(n):
            h = matrix[0][j]
            dfs(0, j, h, p, m, n)
            h = matrix[m-1][j]
            dfs(m-1, j, h, a, m, n)
        for i in range(m):
            h = matrix[i][0]
            dfs(i, 0, h, p, m, n)
            h = matrix[i][n-1]
            dfs(i, n-1, h, a, m, n)
        
        ans = []
        for i in range(m):
            for j in range(n):
                if p[i][j] and a[i][j]:
                    ans.append([i, j])
        return ans