class Solution:
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        def cross_product(a, b, c):
            abx, aby = b[0] - a[0], b[1] - a[1]
            cbx, cby = b[0] - c[0], b[1] - c[1]

            return abx * cby - aby * cbx 

        n = len(points)
        
        positive = False
        negative = False
        
        for i in range(n):
            a = points[i]
            b = points[(i+1) % n]
            c = points[(i+2) % n]
            
            sign = cross_product(a, b, c)
            if sign > 0:
                positive = True
            elif sign < 0:
                negative = True
            
            if positive and negative: return False
        
        return True         