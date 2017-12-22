class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return True
        last_bit = -1
        while n != 0:
            bit = n % 2
            if last_bit != -1:
                if bit == last_bit:
                    return False
                else:
                    last_bit = bit
            else:
                last_bit = bit
            n //= 2
        return True