class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(m, n):
            if n == 0:
                return m
            else:
                return gcd(n, m%n)
        
        
        d = collections.defaultdict(int)
        for num in deck:
            d[num] += 1
            
        keys = list(d.keys())
        
        if len(keys) == 1: return d[keys[0]] >= 2
        
        g = gcd(d[keys[0]], d[keys[1]])
        
        for i in range(2, len(keys)):
            g = gcd(g, d[keys[i]])
        
        return g >= 2