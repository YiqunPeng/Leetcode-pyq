class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return 
        
        inf = 2 ** 31 - 1
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        queue = collections.deque()
        
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0: queue.append((i, j, 0))
                    
        while queue:
            i, j, dis = queue.popleft()
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (0 <= ni < m and 0 <= nj < n and rooms[ni][nj] == inf):
                    rooms[ni][nj] = dis + 1
                    queue.append((ni, nj, dis + 1))