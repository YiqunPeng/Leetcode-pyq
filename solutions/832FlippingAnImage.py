class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(A)
        ans = [[0 for i in range(n)] for j in range(n)]
        
        for i in range(n):
            for j in range(n):
                ans[i][j] = A[i][n-1-j]

        for i in range(n):
            for j in range(n):
                ans[i][j] = 1 - ans[i][j]
        
        return ans