class Solution:
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        modulo = 10 ** 9 + 7
        
        s = 0
        
        A.sort()
        
        for i in range(len(A)):
            s = s - A[i] * (1 << (len(A) - i - 1)) + A[i] * (1 << i)
    
        return s % modulo
                