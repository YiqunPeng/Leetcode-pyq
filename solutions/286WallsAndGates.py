class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return
        
        inf = 2 ** 31 - 1
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m, n = len(rooms), len(rooms[0])
        
        q = collections.deque()   
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
        
        while q:
            i, j, dis = q.popleft()
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and rooms[ni][nj] == inf:
                    rooms[ni][nj] = dis + 1
                    q.append((ni, nj, dis + 1))            