class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        ans = 0
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        
        for i in range(L, R+1):
            cnt = 0
            while i != 0:
                cnt += 1
                i = i & (i - 1)
            if cnt in primes:
                ans += 1
        
        return ans