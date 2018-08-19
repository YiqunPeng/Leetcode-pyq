class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a_sum, b_sum = sum(A), sum(B)
        
        d = (a_sum - b_sum) // 2
        
        a = set(A)
        b = set(B)
        
        for i in a:
            if i - d in b:
                return [i, i - d]