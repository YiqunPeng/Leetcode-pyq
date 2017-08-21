class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums, digits = 9, 1
        while n - nums * digits > 0:
            n = n - nums * digits
            nums *= 10
            digits += 1
        num = 10 ** (digits - 1) + (n - 1) / digits
        return int(str(num)[(n-1) % digits])