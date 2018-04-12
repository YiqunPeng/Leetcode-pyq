class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bit = 0
        index = 31
        ans = 0
        while n != 0:
            bit = n & 1
            ans += bit * 2 ** index
            index -= 1
            n = n >> 1
        
        return ans