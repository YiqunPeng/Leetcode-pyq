class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.row, self.col = 0, 0
        if matrix:
            self.row = len(matrix)
            if matrix[0]:
                self.col = len(matrix[0])
        self.tree = [[0 for j in range(self.col+1)] for i in range(self.row+1)]
        for i in range(self.row):
            for j in range(self.col):
                self.update(i, j, matrix[i][j])
        
    
    def read(self, row, col):
        res = 0
        while row > 0:
            col1 = col
            while col1 > 0:
                res += self.tree[row][col1]
                col1 -= (col1 & -col1)
            row -= (row & -row)
        return res
        
    
    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        ori = self.read(row+1, col+1) + self.read(row, col) - self.read(row, col+1) - self.read(row+1, col)
        val -= ori
        row += 1
        col += 1
        while row <= self.row:
            col1 = col
            while col1 <= self.col:
                self.tree[row][col1] += val
                col1 += (col1 & -col1)
            row += (row & -row)
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.read(row2+1, col2+1) - self.read(row2+1, col1) - self.read(row1, col2+1) + self.read(row1, col1)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
