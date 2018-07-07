class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0: return
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = sys.maxsize
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = sys.maxsize
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == sys.maxsize:
                    matrix[i][j] = 0
