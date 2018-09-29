class Solution:
    # dp
    # time: O(m * n * N)
    # space: O(m * n * N)
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int 
        """
        if N == 0: return 0
        
        mod = 10 ** 9 + 7
        x, y = i, j
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        dp = [[[0 for j in range(n)] for i in range(m)] for k in range(N + 1)] 
        for i in range(m):
            for j in range(n):
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if ni < 0 or ni >= m or nj < 0 or nj >= n:
                        dp[1][i][j] += 1
    
        for k in range(2, N + 1):
            for i in range(m):
                for j in range(n):
                    for d in directions:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < m and 0 <= nj < n:
                            dp[k][i][j] += dp[k-1][ni][nj]

        return sum(i[x][y] % mod for i in dp) % mod
        
        
    # dfs + memo
    # time: O(n * m * N)
    # space: O(n * m * N)
    # def findPaths(self, m, n, N, i, j):
    #     """
    #     :type m: int
    #     :type n: int
    #     :type N: int
    #     :type i: int
    #     :type j: int
    #     :rtype: int
    #     """
    #     self.mod = 10 ** 9 + 7

    #     memo = collections.defaultdict(int)

    #     def dfs(m, n, N, i, j):
    #         if i < 0 or i >= m or j < 0 or j >= n:
    #             return 1

    #         if N == 0: return 0
    #         if (i, j, N) in memo: return memo[(i, j, N)]

    #         directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    #         for d in directions:
    #             ni, nj = i + d[0], j + d[1]
    #             memo[(i, j, N)] = (memo[(i, j, N)] + dfs(m, n, N-1, ni, nj) % self.mod) % self.mod

    #         return memo[(i, j, N)]

    #     return dfs(m, n, N, i, j)