class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ma, na = len(A), len(A[0])
        mb, nb = len(B), len(B[0])
        
        ans = [[0 for j in range(nb)] for i in range(ma)]
        
        compressedA = [{} for i in range(ma)]
        for i in range(ma):
            for j in range(mb):
                if A[i][j] != 0:
                    compressedA[i][j] = A[i][j]
        compressedB = [{} for j in range(nb)]
        for j in range(nb):
            for i in range(na):
                if B[i][j] != 0:
                    compressedB[j][i] = B[i][j]
        
        for i in range(ma):
            for j in range(nb):
                a, b = compressedA[i], compressedB[j]
                if not a or not b: continue
                for k in a:
                    if k in b:
                        ans[i][j] += a[k] * b[k]
        
        return ans
        