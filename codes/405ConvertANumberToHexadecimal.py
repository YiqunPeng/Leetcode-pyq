class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        
        ans = ''
        
        max_int = (1 << 32) - 1
        if num < 0:
            num = max_int + num + 1

        while num != 0:
            r = num % 16
            if r < 10:
                ans += str(r)
            else:
                ans += (chr(ord('a')+r-10))
            num //= 16
        
        return ans[::-1]