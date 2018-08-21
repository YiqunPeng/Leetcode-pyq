class Solution(object):
    # memorized dfs
    # time: O(m * n) m, n -- size of the matrix
    # space: O(m * n)
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            curr = matrix[i][j]
            if not dp[i][j]:
                dp[i][j] = 1 + max(
                    dfs(i-1, j) if i and matrix[i-1][j] < curr else 0,
                    dfs(i+1, j) if i + 1 < m and matrix[i+1][j] < curr else 0,
                    dfs(i, j-1) if j and matrix[i][j-1] < curr else 0,
                    dfs(i, j+1) if j + 1 < n and matrix[i][j+1] < curr else 0)
            
            return dp[i][j]
            
        
        if not matrix or not matrix[0]: return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        
        return max(dfs(i, j) for i in range(m) for j in range(n))
