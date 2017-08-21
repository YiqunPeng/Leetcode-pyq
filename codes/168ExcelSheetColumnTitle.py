class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        digits = 0
        min_num = 1
        ans = ''
        while min_num <= n:
            digits += 1
            min_num += 26 ** digits

        for i in xrange(digits, 0, -1):
            if i == 1: n += 1
            val = 26
            while (val * (26 ** (i-1)) - n) >= 0:
                val -= 1
            print(val * 26 ** (i-1))
            n = n - val * 26 ** (i-1)
            ans += chr(ord('A') + val - 1)
            
        return ans
            