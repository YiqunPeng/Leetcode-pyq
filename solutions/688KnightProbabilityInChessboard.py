class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp = [[1] * N for i in range(N)]
        
        directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
        
        for k in range(K):
            ndp = [[0] * N for i in range(N)]
            
            for i in range(N):
                for j in range(N):
                    for d in directions:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < N and 0 <= nj < N:
                            ndp[i][j] += dp[ni][nj]
            
            dp = ndp
        
        return dp[r][c] / (8 ** K)