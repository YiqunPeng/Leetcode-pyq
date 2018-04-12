class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def transform(n):
            res = 0
            while n != 0:
                res += ((n%10) ** 2)
                n /= 10
            return res
        
        if n == 1: return True
        dic = {n:"1"}
        n = transform(n)
        while not dic.has_key(n):
            dic[n] = 1
            n = transform(n)
            if n == 1:
                return True
        return False