class Solution:
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(maze), len(maze[0])
        v = [[False for j in range(n)] for i in range(m)]
        
        
        def blocked(pos):
            m, n = len(maze), len(maze[0])
            x, y = pos[0], pos[1]
            if x < 0 or x >= m or y < 0 or y >= n:
                return True
            if maze[x][y] == 1:
                return True
            return False 
        
        def dfs(pos, di, v):
            res = False
            n_pos = [pos[0]+d[di][0], pos[1]+d[di][1]]
            if not blocked(n_pos) and v[n_pos[0]][n_pos[1]]: return res

            if not blocked(n_pos):
                res = res or dfs(n_pos, di, v)
            else:
                if pos == destination:
                    return True
                v[pos[0]][pos[1]] = True
                for i in range(1, 4):
                    n_d = (i + di) % 4
                    n_pos = [pos[0]+d[n_d][0], pos[1]+d[n_d][1]]
                    if not blocked(n_pos) and not v[n_pos[0]][n_pos[1]]:
                        res = res or dfs(n_pos, n_d, v)
    
            return res
      
    
        v[start[0]][start[1]] = True
        for i in range(4):
            res = dfs(start, i, v)
            if res:
                return True
        return False
        
        