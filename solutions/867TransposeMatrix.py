class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not A[0]: return A
        
        m, n = len(A), len(A[0])
        ans = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(n):
            for j in range(m):
                ans[i][j] = A[j][i]
        
        return ans
