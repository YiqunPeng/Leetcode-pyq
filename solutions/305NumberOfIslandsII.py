class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def find(i, j):
            if positions[parents[i, j]] != [i, j]:
                pi, pj = positions[parents[i, j]]
                parents[i, j] = find(pi, pj)
            return parents[i, j]
        
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        islands = 0
        ans = []     
        seen = set()
        parents = {}
        
        for idx, [i, j] in enumerate(positions):
            seen.add((i, j))
            neighbors = set()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) in seen:
                    neighbors.add(find(ni, nj))
            
            if len(neighbors) == 0:
                islands += 1
                parents[i, j] = idx
            else:
                islands -= len(neighbors) - 1       
                min_idx = min(neighbors)
                for neighbor in neighbors:
                    pi, pj = positions[neighbor]
                    parents[pi, pj] = min_idx
                parents[i, j] = min_idx
                
            ans.append(islands)
            
        return ans