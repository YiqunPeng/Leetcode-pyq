from heapq import heappop, heappush

class Solution:
    # min heap
    # time: O(n ^ 2)
    # space: O(n ^ 2)
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """    
        n = len(grid)
        
        ans = 0
        visited = set([(0, 0)])
        
        pq = [(grid[0][0], 0, 0)]
        while pq:
            t, x, y = heappop(pq)
            ans = max(ans, t)
            
            if x == y == n - 1: 
                return ans
            
            for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                n_x, n_y = x + d[0], y + d[1]
                if not (0 <= n_x < len(grid) and 0 <= n_y < len(grid[0])): continue
                
                if (n_x, n_y) not in visited:
                    heappush(pq, (grid[n_x][n_y], n_x, n_y))
                    visited.add((n_x, n_y))
        
        return n * n - 1
        
        
    # binary search + dfs
    # time: O(logn^2 * n^2) n -- length of the grid
    # space: O(n^2)
    # def swimInWater(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     def dfs(x, y, t, visited):
    #         if x == y == len(grid) - 1: 
    #             return True

    #         visited.add((x, y))

    #         directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    #         for d in directions:
    #             n_x, n_y = x + d[0], y + d[1]
    #             if not (0 <= n_x < len(grid) and 0 <= n_y < len(grid[0])): continue
    #             if (n_x, n_y) in visited: continue

    #             if grid[n_x][n_y] <= t:
    #                 if dfs(n_x, n_y, t, visited): return True

    #         return False

    #     left, right = grid[0][0], len(grid) * len(grid) - 1
    #     while left < right:
    #         mid = left + (right - left) // 2
    #         if dfs(0, 0, mid, set()): 
    #             right = mid
    #         else:
    #             left = mid + 1

    #     return right
