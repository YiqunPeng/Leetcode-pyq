class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        min_r = [sys.maxsize] * n
        min_r[-1] = A[-1]
        for i in range(n-2, -1, -1):
            min_r[i] = min(min_r[i+1], A[i])
        
        max_l = A[0]
        for i in range(n - 1):
            if max_l <= min_r[i+1]:
                return i + 1
            max_l = max(max_l, A[i])