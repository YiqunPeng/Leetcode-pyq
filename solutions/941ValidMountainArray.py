class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n < 3: return False
        
        peak = -1
        for i in range(1, n - 1):
            if A[i] <= A[i-1]: return False
            if A[i] > A[i+1]:
                peak = i
                break
 
        if peak == -1: return False
        
        for i in range(peak + 1, n):
            if A[i] >= A[i-1]: return False
        
        return True