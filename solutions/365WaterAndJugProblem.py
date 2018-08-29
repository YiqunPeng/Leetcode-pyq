class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(m, n):
            if n == 0: 
                return m
            else:
                return gcd(n, m % n)
            
        if z == 0: return True
        if x == y == 0:
            if z == 0: 
                return True
            else:
                return False
        
        x, y = max(x, y), min(x, y)
        
        if gcd(x, y) == 1:
            if 1 <= z <= x + y:
                return True
            else:
                return False
        
        else:
            if z % gcd(x, y) == 0:
                return True
            else:
                return False