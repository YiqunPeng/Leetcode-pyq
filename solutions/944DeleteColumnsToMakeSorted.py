class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        rows, cols = len(A), len(A[0])
        if rows == 1: return 0
        
        ans = 0
        for j in range(cols):
            sort = True
            for i in range(1, rows):
                if A[i][j] < A[i-1][j]:
                    sort = False
                    break
            if not sort: ans += 1
        
        return ans