from bisect import bisect_left, bisect_right

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        
        col = bisect_right(matrix[0], target)
        left = [i[0] for i in matrix]
        row = bisect_right(left, target)

        for i in range(row):
            if matrix[i][0] <= target <= matrix[i][col-1]:
                pos = bisect_left(matrix[i], target, 0, col)
                if matrix[i][pos] == target:
                    return True
        
        return False
