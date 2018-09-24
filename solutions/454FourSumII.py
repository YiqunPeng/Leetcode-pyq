class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ab = collections.defaultdict(int)
        cd = collections.defaultdict(int)
        
        n = len(A)
        
        for i in range(n):
            for j in range(n):
                ab[A[i]+B[j]] += 1
                cd[C[i]+D[j]] += 1
        
        ans = 0
        for kab, vab in ab.items():
            ans = ans + vab * cd[-kab]
        return ans  