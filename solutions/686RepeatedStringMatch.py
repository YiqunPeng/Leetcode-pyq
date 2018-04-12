class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        times = len(B) // len(A)
        new_A = A * times
        for i in range(times, times+3):
            if B in new_A:
                return i
            else:
                new_A = new_A + A
        return -1