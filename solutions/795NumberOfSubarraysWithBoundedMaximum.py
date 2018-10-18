class Solution:
    # dp
    # time: O(n)
    # space: O(1)
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """    
        if not A: return 0
        
        n = len(A)
        pre = -1
        curr = 0
        ans = 0
        
        for i in range(1, n + 1):
            if A[i-1] < L:
                ans += curr
            elif A[i-1] > R:
                pre = i - 1
                curr = 0
            else:
                curr = i - 1 - pre
                ans += curr
        
        return ans
        

    # dp
    # time: O(n)
    # space: O(n)
    # def numSubarrayBoundedMax(self, A, L, R):
    #     """
    #     :type A: List[int]
    #     :type L: int
    #     :type R: int
    #     :rtype: int
    #     """
    #     if not A: return 0

    #     n = len(A)
    #     dp = [0] * (n + 1)

    #     pre = -1

    #     for i in range(1, n + 1):
    #         if A[i-1] < L:
    #             dp[i] = dp[i-1]
    #         elif A[i-1] > R:
    #             pre = i - 1
    #         else:
    #             dp[i] = i - 1 - pre

    #     return sum(dp)      