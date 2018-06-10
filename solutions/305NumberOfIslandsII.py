class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        grid = [[-1 for j in range(n)] for i in range(m)]
        father = []
        ans = []
        
        def find(i1):
            if father[i1] == i1:
                return i1
            else:
                father[i1] = find(father[i1])
                return father[i1]
            
        cnt = 0
        i_num = 0
        
        for x, y in positions:
            new_island_flag = True
            neighbor = set()
            for n_x, n_y in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if not (0 <= n_x < m and 0 <= n_y < n): continue
                if grid[x][y] == -1 and grid[n_x][n_y] >= 0:
                    new_island_flag = False
                    grid[x][y] = find(grid[n_x][n_y])
                elif grid[x][y] >= 0 and grid[n_x][n_y] >= 0:
                    f_xy, f_nxy = find(grid[x][y]), find(grid[n_x][n_y])
                    if f_nxy not in neighbor and f_xy != f_nxy:
                        father[f_xy] = f_nxy
                        i_num -= 1
                        neighbor.add(f_nxy)
            if new_island_flag:
                father.append(cnt)
                grid[x][y] = cnt
                cnt += 1
                i_num += 1
            ans.append(i_num)
        
        return ans
        