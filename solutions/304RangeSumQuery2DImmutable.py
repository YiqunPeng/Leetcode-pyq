class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.row, self.col = 0, 0
        if matrix: self.row = len(matrix)
        if matrix and matrix[0]: self.col = len(matrix[0])
        self.pre_sum = [[0 for j in range(self.col+1)] for i in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                self.pre_sum[i][j+1] = self.pre_sum[i][j] + matrix[i][j]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for i in range(row1, row2+1):
            res += (self.pre_sum[i][col2+1] - self.pre_sum[i][col1])
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
