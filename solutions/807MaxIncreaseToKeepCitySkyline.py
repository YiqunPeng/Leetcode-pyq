class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top, left = [-1 for i in range(len(grid[0]))], [-1 for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                left[i] = max(left[i], grid[i][j])
                top[j] = max(top[j], grid[i][j])
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += (min(top[j], left[i]) - grid[i][j])
        
        return ans