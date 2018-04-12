class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        def digits(num):
            return len(str(num))
    
        def count(num, d, dic):
            if d == 1:
                if num == 0:
                    return 0
                else:
                    return 1
            high = num // (10 ** (d - 1))
            low = num % (10 ** (d - 1))
            low_9 = 10 ** (d - 1)
            cnt_low_9 = 0
            if dic.has_key(low_9):
                cnt_low_9 = dic[low_9]
            else:
                cnt_low_9 = count(low_9, d-1, dic)
                dic[low_9] = cnt_low_9
            if high == 1:
                return 1 + low + count(low, digits(low), dic) + cnt_low_9
            else:
                return 10**(d-1) + count(low, digits(low), dic) + high*cnt_low_9
                
        
    
        if n <= 0: return 0
         
        dic = {}
        
        return count(n, digits(n), dic)
        
        