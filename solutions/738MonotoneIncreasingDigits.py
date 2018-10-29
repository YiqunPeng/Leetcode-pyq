class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        N = str(N)
        length = len(N)
        
        if length == 1: return int(N)

        pos = 1
        while pos < length and N[pos] >= N[pos - 1]:
            pos += 1
        
        if pos == length: return int(N)
        
        pos -= 1
        while pos > 0 and N[pos] == N[pos - 1]:
            pos -= 1
        
        return int(N[:pos] + str(int(N[pos]) - 1) + '9' * (length - pos - 1))