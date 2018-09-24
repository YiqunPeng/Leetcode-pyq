class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0: return "NaN"
        if numerator == 0: return '0'
        
        sign = numerator // abs(numerator) * denominator // abs(denominator)
        if sign == -1:
            sign = '-'
        else:
            sign = ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        d = numerator // denominator
        m = numerator % denominator
        
        if m == 0:
            return sign + str(d)
        else:
            m *= 10
        
        res = ''
        dic = {}
        while m not in dic and m != 0:
            div = m // denominator
            dic[m] = len(res)
            res = res + str(div)
            m = m % denominator * 10
        
        if m != 0:
            idx = dic[m]
            res = res[:idx] + '(' + res[idx:] + ')'
        return sign + str(d) + '.' + res