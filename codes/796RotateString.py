class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # return A in B + B
        
        if len(A) != len(B): return False

        if A == B: return True
        
        r_A = A[1:] + A[0]
        
        while r_A != A:
            if r_A == B:
                return True
            r_A = r_A[1:] + r_A[0]
            
        return False
        