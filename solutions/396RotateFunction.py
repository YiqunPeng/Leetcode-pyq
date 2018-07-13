class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sum_a = sum(A)
        n = len(A)
        
        pre = 0
        for i in range(n):
            pre += i * A[i]
        ans = pre
        
        for i in range(n):
            curr = pre + sum_a - n * A[n - 1 - i]
            ans = max(curr, ans)
            pre = curr
        
        return ans