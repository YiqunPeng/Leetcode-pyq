class Solution: 
    # bfs
    # time: O(k) k -- number of elements in the matrix
    # space: O(k)
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]: return None
        
        m, n = len(matrix), len(matrix[0])
        
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i, j, 0))
                else:
                    matrix[i][j] = sys.maxsize
        
        while queue:
            i, j, dis = queue.popleft()
            
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for d in directions:
                n_i, n_j = i + d[0], j + d[1]
                if not (0 <= n_i < m and 0 <= n_j < n and matrix[n_i][n_j] == sys.maxsize): continue
                
                matrix[n_i][n_j] = dis + 1
                queue.append((n_i, n_j, dis + 1))
        
        return matrix