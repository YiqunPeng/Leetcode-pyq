class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    ans += self.count_perimeter(grid, r, c)
        
        return ans
    
    def count_perimeter(self, grid, r, c):
        block = 0
        if (r-1)>=0 and grid[r-1][c] == 1:
            block += 1
        if (r+1)<len(grid) and grid[r+1][c] == 1:
            block += 1
        if (c-1)>=0 and grid[r][c-1] == 1:
            block += 1
        if (c+1)<len(grid[0]) and grid[r][c+1] == 1:
            block += 1
        return 4 - block
        