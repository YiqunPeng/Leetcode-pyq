class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        ans = []
        mode = 0    #0-up 1-down
        num = len(matrix) * len(matrix[0])
        row, col = 0, 0
        for i in xrange(num):
            ans.append(matrix[row][col])
            if mode == 0:
                if row == 0 and col != len(matrix[0])-1:
                    col += 1
                    mode = 1
                    continue
                if col == len(matrix[0])-1:
                    row += 1
                    mode = 1
                    continue
                row -= 1
                col += 1
            if mode == 1:
                if col == 0 and row != len(matrix)-1:
                    row += 1
                    mode = 0
                    continue
                if row == len(matrix)-1:
                    col += 1
                    mode = 0
                    continue
                row += 1
                col -= 1
        return ans
            
                
                    