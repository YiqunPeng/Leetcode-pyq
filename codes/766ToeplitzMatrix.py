class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row, col = len(matrix), len(matrix[0])
        
        for i in range(col):
            x, y = 0, i
            while x+1<row and y+1<col:
                if matrix[x][y] != matrix[x+1][y+1]:
                    return False
                x += 1
                y += 1
        
        for j in range(1, row):
            x, y = j, 0
            while x+1<row and y+1<col:
                if matrix[x][y] != matrix[x+1][y+1]:
                    return False
                y += 1
                x += 1
        
        return True
            