class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        max_int_p = '2147483647'
        max_int_n = '2147483648'
        sign = x / abs(x)
        x = abs(x)
        s = ''
        while x != 0:
            s += str(x % 10)
            x /= 10
        lenS = len(s)
        if (sign == 1 and lenS > 9 and s > max_int_p) or (sign == -1 and lenS > 9 and s > max_int_n):
            return 0
        while s[0] == '0':
            s = s[1:]
        return int(s) * sign
            