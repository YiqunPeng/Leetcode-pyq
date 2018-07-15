class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        num = set()
        
        v = 1
        while v <= 10 ** 9:
            h = [0] * 10
            t = v 
            while t > 0:
                h[t%10] += 1
                t //= 10
            num.add(str(h))
            v = v * 2
        
        h = [0] * 10
        N = str(N)
        for n in N:
           h[int(n)] += 1
        
        return str(h) in num