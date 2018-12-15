class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        
        top, front, side = 0, 0, 0
        
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]: top += 1
        
        for row in grid:
            side += max(row)
            
        for row in zip(*grid):
            top += max(row)
            
        return top + front + side       