class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        
        n_1 = self.grayCode(n-1)
        return n_1 + [i+2**(n-1) for i in n_1[::-1]]