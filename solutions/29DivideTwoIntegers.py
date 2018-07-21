class Solution:
    # binary search
    # time: O(logn)
    # space: O(1)
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        ans = 0   
        while dividend >= divisor:
            tmp = divisor
            cnt = 1
            while tmp <= dividend:
                tmp = tmp << 1
                cnt = cnt << 1
            ans += cnt >> 1
            dividend -= tmp >> 1
        
        if not sign: ans = ~ans + 1
        return min(ans, (1 << 31) - 1)