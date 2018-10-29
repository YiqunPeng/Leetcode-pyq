class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        dp = A[0]
        
        for i in range(1, n):
            nxt = dp[:]
            for j in range(n):
                nxt[j] = dp[j] + A[i][j]
                if j - 1 >= 0:
                    nxt[j] = min(nxt[j], dp[j-1] + A[i][j])
                if j + 1 < n:
                    nxt[j] = min(nxt[j], dp[j+1] + A[i][j])
            dp = nxt
        
        return min(dp)