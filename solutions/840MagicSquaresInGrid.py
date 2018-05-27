class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def is_magic(i, j):
            v = [0] * 10
            for m in range(3):
                for n in range(3):
                    val = grid[i+m][j+n]
                    if 1 <= val <= 9:
                        v[val] = 1
            for k in range(1, 10):
                if v[k] == 0:
                    return False
            s = sum(grid[i][j:j+3])
            if s != sum(grid[i+1][j:j+3]) or s != sum(grid[i+2][j:j+3]):
                return False
            c1, c2, c3 = 0, 0, 0
            for k in range(3):
                c1 += grid[i+k][j]
                c2 += grid[i+k][j+1]
                c3 += grid[i+k][j+2]
            if s != c1 or s != c2 or s != c3:
                return False
            d1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
            d2 = grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
            if s != d1 or s != d2:
                return False
            return True
            
        
        n = len(grid)
        ans = 0
        
        for i in range(n-2):
            for j in range(n-2):
                if is_magic(i, j):
                    ans += 1
        
        return ans
        