class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        
        temp_x = x
        d = 0
        while temp_x != 0:
            d += 1
            temp_x //= 10
        
        half_d = d // 2
        for i in range(half_d):
            low = x % 10
            high = x // (10 ** (d - 1))
            if low != high:
                return False
            else:
                x = x - high * (10 ** (d - 1))
                x = x // 10
                d -= 2
        
        return True
