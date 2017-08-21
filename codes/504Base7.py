class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        
        if num < 0:
            neg = 1
            num = -num
        else:
            neg = 0
        
        ans = ''
        
        enum = [7 ** i for i in xrange(9)]
        pos = 8
        while num < enum[pos]:
            pos -= 1
        while pos >= 0:
            val = 6
            while val * enum[pos] > num:
                val -= 1
            ans += str(val)
            num -= val * enum[pos]
            pos -= 1
        
        if neg == 1:
            return '-' + ans
        else:
            return ans