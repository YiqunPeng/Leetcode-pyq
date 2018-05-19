class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0 for i in range(n)] for j in range(n)]
        v = [[False for i in range(n)] for j in range(n)]
        
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        c = 0
        
        i, j = 0, 0
        val = 1
        
        while val <= n * n:
            ans[i][j] = val
            v[i][j] = True
            val += 1
            
            n_i, n_j = d[c][0] + i, d[c][1] + j
            
            if 0 <= n_i < n and 0 <= n_j < n and not v[n_i][n_j]:
                i, j = n_i, n_j
            else:
                for k in range(3):
                    n_c = (c + k + 1) % 4
                    n_i, n_j = d[n_c][0] + i, d[n_c][1] + j
                    if 0 <= n_i < n and 0 <= n_j < n and not v[n_i][n_j]:
                        c = n_c
                        i, j = n_i, n_j
                        break

        return ans
                