class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        k = 1
        while q * k % p != 0:
            k += 1
            
        if q * k // p % 2 == 1 and k % 2 == 0:
            return 2
        
        if q * k // p % 2 == 1 and k % 2 == 1:
            return 1
        
        if q * k // p % 2 == 0 and k % 2 == 1:
            return 0  