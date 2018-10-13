class Solution:
    # dfs
    # time: O(m * n)
    # space: O(m * n)
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j, m, n):
            visited.add((i, j))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1' and (ni, nj) not in visited:
                    dfs(ni, nj, m, n)
        
        
        if not grid: return 0 
        ans = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j, m, n)
                    ans += 1
        return ans
    
    
    # union find
    # time: O(m * n)
    # space: O(m * n)
    # def numIslands(self, grid):
    #     """
    #     :type grid: List[List[str]]
    #     :rtype: int
    #     """
    #     def find(pos):
    #         if father[pos] != pos:
    #             father[pos] = find(father[pos])
    #         return father[pos]


    #     def union(p1, p2):
    #         fp1, fp2 = find(p1), find(p2)
    #         if fp1 == fp2: return
    #         father[fp2] = find(fp1)


    #     if not grid: return 0
    #     m, n = len(grid), len(grid[0])    
    #     father = {(i, j): (i, j) for i in range(m) for j in range(n) if grid[i][j] == '1'}

    #     directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == '0': continue
    #             for d in directions:
    #                 ni, nj = i + d[0], j + d[1]
    #                 if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
    #                     union((i, j), (ni, nj))

    #     ans = 0
    #     for k, v in father.items():
    #         if k == v: ans += 1
    #     return ans