class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        
        ans = int(math.sqrt(2 * n))
        while (ans + 1) * ans / 2 > n:
            ans -= 1
        return ans