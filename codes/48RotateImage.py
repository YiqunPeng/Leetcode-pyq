class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        half_n = n // 2
        
        for i in range(half_n):
            for j in range(i, n-i-1):
                temp_i, temp_j = i, j
                temp_val = matrix[temp_i][temp_j]
                for k in range(4):
                    new_i = temp_j
                    new_j = n - 1 - temp_i
                    new_val = matrix[new_i][new_j]
                    matrix[new_i][new_j] = temp_val
                    temp_i = new_i
                    temp_j = new_j
                    temp_val = new_val

        
                
                    