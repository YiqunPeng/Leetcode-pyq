class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res_dic = {0: 1, 1: x}
        
        def power(x, n):
            if n in res_dic:
                return res_dic[n]
            
            if n % 2 == 0:
                res_dic[n] = power(x, n//2) * power(x, n//2)
            else:
                res_dic[n] = power(x, n//2) * power(x, n//2) * x
            
            return res_dic[n]
                
        if n < 0:
            return 1 / power(x, -n)
        else:
            return power(x, n)
