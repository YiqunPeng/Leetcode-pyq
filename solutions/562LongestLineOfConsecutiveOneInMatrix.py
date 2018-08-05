class Solution(object):
    # array
    # time: O(m * n) m, n -- size of the matrix
    # space: O(m * n)
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        ans = 0
        
        if not M or not M[0]: return ans
        m, n = len(M), len(M[0])
        
        ones = [[[0, 0, 0, 0] for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if M[i][j] == 0: continue
                ones[i][j] = [1, 1, 1, 1]
                
                if i - 1 >= 0 and M[i-1][j]:
                    ones[i][j][0] = ones[i-1][j][0] + 1
                if j - 1 >= 0 and M[i][j-1]:
                    ones[i][j][1] = ones[i][j-1][1] + 1
                if i - 1 >= 0 and j - 1 >= 0 and M[i-1][j-1]:
                    ones[i][j][2] = ones[i-1][j-1][2] + 1
                if i - 1 >= 0 and j + 1 < n and M[i-1][j+1]:
                    ones[i][j][3] = ones[i-1][j+1][3] + 1

                ans = max(ans, max(ones[i][j]))

        return ans
