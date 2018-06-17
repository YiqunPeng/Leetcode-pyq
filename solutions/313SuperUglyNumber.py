class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1: return 1
        
        dp = [0] * n
        dp[0] = 1
   
        pq = [1]
        heapq.heapify(pq)
        pre = heapq.heappop(pq)
        
        for i in range(1, n):
            for p in primes:
                heapq.heappush(pq, pre*p)
            dp[i] = heapq.heappop(pq)
            while pre >= dp[i]:
                dp[i] = heapq.heappop(pq)
            pre = dp[i]
        
        return dp[-1]