class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        
        min_v, max_v = A[0], A[-1]
        ans = max_v - min_v
        
        for i in range(len(A) - 1):
            min_v = min(A[0] + 2 * K, A[i + 1])
            max_v = max(max_v, A[i] + 2 * K)
            
            ans = min(ans, max_v - min_v)
        
        return ans