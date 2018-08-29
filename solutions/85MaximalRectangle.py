class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        
        n, m = len(matrix), len(matrix[0])
        ans = 0
        
        heights = [0] * (m + 1)
        for i in range(n):
            stack = [-1]
            
            for j in range(m + 1):
                if j < m and i == 0:
                    heights[j] = int(matrix[i][j])
                elif j < m:
                    if matrix[i][j] == '1':
                        heights[j] += 1
                    else:
                        heights[j] = 0

                while heights[stack[-1]] > heights[j]:
                    pos = stack.pop()
                    ans = max(ans, (j - 1 - stack[-1]) * heights[pos])
                
                stack.append(j)
        
        return ans