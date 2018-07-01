class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(len(A)):
            if A[i][0] == 0:
                for j in range(len(A[0])):
                    A[i][j] = 1 - A[i][j]

        for j in range(len(A[0])):
            cnt = 0
            for i in range(len(A)):
                if A[i][j] == 0:
                    cnt += 1
            if len(A) - cnt < cnt:
                for i in range(len(A)):
                    A[i][j] = 1 - A[i][j]

        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                ans += A[i][j] * 2 ** (len(A[0]) - 1 - j)
        return ans
        