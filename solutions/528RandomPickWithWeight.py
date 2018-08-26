class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.pre_sum = [0] * len(w)
        self.pre_sum[0] = w[0]
        for i in range(1, len(w)):
            self.pre_sum[i] = self.pre_sum[i-1] + w[i]
        

    def pickIndex(self):
        """
        :rtype: int
        """
        t = random.randint(1, self.pre_sum[-1])
        
        l, r = 0, len(self.pre_sum) - 1
        while l <= r:
            m = l + (r - l) // 2
            if (m == 0 and t <= self.pre_sum[m]) or (self.pre_sum[m-1] < t <= self.pre_sum[m]):
                return m
            
            if self.pre_sum[m] < t:
                l = m + 1
            else:
                r = m - 1
        
        return r


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()