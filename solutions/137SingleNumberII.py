class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [0] * 32
        
        ans = 0
        for i in range(0, 32):
            s = 0
            for num in nums:
                if (num >> i) & 1 == 1:
                    s = (s + 1) % 3
            
            if s != 0:
                ans |= (s << i)

        if ans & (1 << 31) != 0:
            return -((~ans + 1) & 0xffffffff)
        else:
            return ans