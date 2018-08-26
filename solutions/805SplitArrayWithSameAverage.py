class Solution:
    # dp
    # time: O(n^2 * n * m) n -- length of A; m -- maximum of A[i]
    # space: O(n^2)
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        a_sum = sum(A)
        
        candi_k = set()
        for i in range(1, n // 2 + 1):
            if a_sum * i % n == 0:
                candi_k.add(i)
        if not candi_k: return False
                
        dp = [[set() for j in range(n // 2 + 1)] for i in range(n + 1)]
        dp[0][0].add(0)
        for i in range(1, n + 1):
            num = A[i - 1]
            dp[i][0].add(0)
            for j in range(1, min(n // 2 + 1, i + 1)):
                for v in dp[i-1][j]:
                    dp[i][j].add(v)
                for v in dp[i-1][j-1]:
                    dp[i][j].add(v + num)
        
        for k in candi_k:
            if a_sum * k // n in dp[n][k]:
                return True
        return False