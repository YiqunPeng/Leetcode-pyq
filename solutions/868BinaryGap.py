class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        b = bin(N)[2:]
        
        ans = 0
        pre = -1
        
        for i in range(len(b)):
            if b[i] == '1':
                if pre == -1:
                    pre = i
                else:
                    ans = max(ans, i - pre)
                    pre = i
        
        return ans