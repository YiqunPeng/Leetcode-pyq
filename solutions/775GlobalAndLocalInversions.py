class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        
        minimum = [sys.maxsize] * n
        minimum[-1] = A[-1]
        for i in range(n-2, -1, -1):
            if A[i] < minimum[i+1]:
                minimum[i] = A[i]
            else:
                minimum[i] = minimum[i+1]
        
        for i in range(n-1):
            if A[i] > A[i+1] and (i + 2 < n and A[i] > minimum[i+2]):
                return False
            if A[i] < A[i+1] and minimum[i+1] < A[i]:
                return False
        
        return True