class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = ''
        nums = [i for i in range(n+1)]
        fac = [1] * n
        
        for i in range(1, n):
            fac[i] = fac[i-1] * i
        
        l = n - 1
        while l >= 0:
            d, m = divmod(k, fac[l])
            if m == 0:
                ans = ans + str(nums.pop(d))
                k = k - (d - 1) * fac[l]
            else:
                ans = ans + str(nums.pop(d+1))
                k = k - d * fac[l]
            l -= 1
            
        return ans