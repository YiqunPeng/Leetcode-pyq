from heapq import heappop, heappush

class Solution:
    # min heap
    # time: O(E + nlogn) E -- number of flights, n -- number of cities
    # space: O(n^2 + n)
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """  
        matrix = [[-1 for i in range(n)] for j in range(n)]
        for f in flights:
            matrix[f[0]][f[1]] = f[2]
        
        heap = [(0, src, K + 1)]
        while heap:
            cost, node, stop = heappop(heap)
            if node == dst:
                return cost
            
            if stop > 0:
                for i in range(n):
                    if matrix[node][i] != -1:
                        heappush(heap, (cost + matrix[node][i], i, stop - 1))
        
        return -1
      
    # dp 
    # time: O(K * n) n -- number of flights
    # space: O(n)
    # def findCheapestPrice(self, n, flights, src, dst, K):
    #     """
    #     :type n: int
    #     :type flights: List[List[int]]
    #     :type src: int
    #     :type dst: int
    #     :type K: int
    #     :rtype: int
    #     """        
    #     dp = [sys.maxsize] * n
    #     dp[src] = 0

    #     for i in range(K + 1):
    #         nxt = dp[:]
    #         for f in flights:
    #             nxt[f[1]] = min(nxt[f[1]], dp[f[0]] + f[2])
    #         dp = nxt

    #     return dp[dst] if dp[dst] != sys.maxsize else -1
      
    
    # dp
    # time: O(K * n)
    # space: O(K * n)
    # def findCheapestPrice(self, n, flights, src, dst, K):
    #     """
    #     :type n: int
    #     :type flights: List[List[int]]
    #     :type src: int
    #     :type dst: int
    #     :type K: int
    #     :rtype: int
    #     """
    #     dp = [[sys.maxsize for j in range(K+1)] for i in range(n)]
    #     dp[src][0] = 0
    #     for f in flights:
    #         if f[0] == src:
    #             dp[f[1]][0] = f[2]

    #     for i in range(1, K + 1):
    #         for f in flights:
    #             dp[f[1]][i] = min(dp[f[1]][i], dp[f[0]][i-1] + f[2], dp[f[1]][i-1])

    #     return dp[dst][K] if dp[dst][K] != sys.maxsize else -1