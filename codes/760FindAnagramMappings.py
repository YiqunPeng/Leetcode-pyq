class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        ans = []
        
        len_a = len(A)
        for i in range(len_a):
            len_b = len(B)
            for j in range(len_b):
                if B[j] == A[i]:
                    ans.append(j)
                    break
                    
        return ans