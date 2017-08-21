class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = int(a.split('+')[0])
        n = int(a.split('+')[1][:-1])
        p = int(b.split('+')[0])
        q = int(b.split('+')[1][:-1])
        
        real = m * p - n * q
        image = m * q + n * p
        
        res = str(real) + '+' + str(image) + 'i'
        return res