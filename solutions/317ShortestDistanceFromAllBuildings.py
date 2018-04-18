class Solution:
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        b_cnt = 0
        b_reach = [[0] * col for i in range(row)]
        dis_sum = [[0] * col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    b_cnt += 1
                    
        
        def bfs(x_s, y_s):
            v = [[False] * col for i in range(row)]
            v[x_s][y_s] = True
            queue = [(x_s, y_s, 0)]
            cnt = 1
            
            while queue:
                x, y, dis = queue.pop(0)
                for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if 0 <= i < row and 0 <= j < col and not v[i][j]:
                        v[i][j] = True
                        if grid[i][j] == 0:
                            dis_sum[i][j] += (dis + 1)
                            queue.append((i, j, dis+1))
                            b_reach[i][j] += 1
                        if grid[i][j] == 1:
                            cnt += 1
            
            return cnt == b_cnt
                              
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and not bfs(i, j):
                    return -1
          
        ans = sys.maxsize
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0 and b_reach[i][j] == b_cnt:
                    ans = min(ans, dis_sum[i][j])
        return ans if ans != sys.maxsize else -1
                        