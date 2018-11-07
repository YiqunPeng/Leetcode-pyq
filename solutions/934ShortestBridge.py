class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        islands = []
        
        def find_islands(i, j):
            seen.add((i, j))
            
            res = []
            queue = collections.deque([(i, j)])
            
            while queue:
                i, j = queue.popleft()
                res.append((i, j))
                
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < m and 0 <= nj < n and A[ni][nj] == 1 and (ni, nj) not in seen:
                        seen.add((ni, nj))
                        queue.append((ni, nj))
                        
            return res
         
            
        def expand_island(island):
            seen = set(island)
            
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            queue = collections.deque()
            for i, j in island:
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                        seen.add((ni, nj))
                        queue.append((ni, nj, 0))
            
            while queue:
                i, j, dis = queue.popleft()
                if A[i][j] == 1: return dis
                
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                        seen.add((ni, nj))
                        queue.append((ni, nj, dis + 1))           
            
 
        m, n = len(A), len(A[0])
        
        seen = set()
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and (i, j) not in seen:
                    islands.append(find_islands(i, j))
         
        return expand_island(islands[0])