class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return 
        m, n = len(rooms), len(rooms[0])
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:       
                    v = set()
                    v.add((i, j))      
                    q = collections.deque()
                    q.append((i, j, 0))
                    while q:
                        x, y, d = q.popleft()
                        for n_i, n_j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                            if not (0 <= n_i < m and 0 <= n_j < n and rooms[n_i][n_j] != -1 and (n_i, n_j) not in v): continue
                            v.add((n_i, n_j))
                            if rooms[n_i][n_j] > d + 1:
                                rooms[n_i][n_j] = d + 1
                                q.append((n_i, n_j, d + 1))
                    
