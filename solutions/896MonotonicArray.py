class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increasing, decreasing = True, True
        
        for i in range(1, len(A)):
            if increasing and A[i] < A[i-1]:
                increasing = False

            if decreasing and A[i] > A[i-1]:
                decreasing = False
        
        return increasing or decreasing