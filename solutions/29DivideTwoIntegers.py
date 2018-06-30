class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if dividend < 0: 
            sign = -sign
            dividend = -dividend
        if divisor < 0:
            sign = -sign
            divisor = -divisor
        
        ans = 0
        
        while dividend >= divisor:
            tmp = divisor
            cnt = 1
            while tmp <= dividend:
                tmp = tmp << 1
                cnt = cnt << 1
            ans += cnt >> 1
            dividend -= tmp >> 1
        
        return min(ans * sign, 2 ** 31 - 1)
