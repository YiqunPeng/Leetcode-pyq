class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        
        m, n = len(matrix), len(matrix[0])
        maxsize = 0
        
        dp = [[0 for j in range(n)] for i in range(2)]
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            maxsize = max(maxsize, dp[0][j])
        
        for i in range(1, m):
            dp[i%2][0] = int(matrix[i][0])
            maxsize = max(maxsize, dp[i%2][0])
            for j in range(1, n):
                if matrix[i][j] == '0':
                    dp[i%2][j] = 0
                else:
                    dp[i%2][j] = min(dp[1-i%2][j], dp[i%2][j-1], dp[1-i%2][j-1]) + 1
                    maxsize = max(maxsize, dp[i%2][j])
        
        return maxsize ** 2
