class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        
        dirc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        mode = 0
        cnt = 0
        m, n = len(matrix), len(matrix[0])
        ans = []
        x, y = 0, -1
        
        while cnt < m * n:
            n_x = x + dirc[mode][0]
            n_y = y + dirc[mode][1]
            if n_x < 0 or n_x >= m or n_y < 0 or n_y >= n or matrix[n_x][n_y] == ' ':
                mode = (mode + 1) % 4
            else:
                cnt += 1
                ans.append(matrix[n_x][n_y])                
                matrix[n_x][n_y] = ' '
                x, y = n_x, n_y
        
        return ans
                
        