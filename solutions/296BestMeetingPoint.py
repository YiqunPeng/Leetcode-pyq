class Solution:
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """       
        row, col = len(grid), len(grid[0])
        row_1, col_1 = [], []
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    row_1.append(i)
                    col_1.append(j)
        
        row_m = sorted(row_1)[len(row_1)//2]
        col_m = sorted(col_1)[len(col_1)//2]
        
        ans = 0      
        for r in row_1:
            ans = ans + abs(r - row_m)
        for c in col_1:
            ans = ans + abs(c - col_m)
        return ans
                