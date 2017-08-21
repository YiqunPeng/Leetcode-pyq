class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        if n <= 2: return 0
        mark_list = [0] * n
        for i in xrange(3, n, 2):
            if mark_list[i] == 0:
                ans += 1
                temp = i + i
                while temp < n:
                    mark_list[temp] = 1
                    temp = temp + i
        return ans+1 if n > 2 else ans