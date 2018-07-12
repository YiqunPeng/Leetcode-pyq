class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 1
        
        for i in range(2, int((2 * N) ** 0.5 + 1)):
            if (N - i * (i-1) / 2) % i == 0:
                ans += 1
        
        return ans
        