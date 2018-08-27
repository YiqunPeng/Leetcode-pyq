class Solution:

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        
        self.pre_sum = [0] * len(rects)
        self.pre_sum[0] = (rects[0][3] - rects[0][1] + 1) * (rects[0][2] - rects[0][0] + 1)
        for i in range(1, len(rects)):
            self.pre_sum[i] = self.pre_sum[i-1] + (rects[i][3] - rects[i][1] + 1) * (rects[i][2] - rects[i][0] + 1) 

            
    def pick_rectangle(self):
        t = random.randint(1, self.pre_sum[-1])

        l, r = 0, len(self.rects) - 1
        while l <= r:
            m = l + (r - l) // 2
            if (m == 0 and self.pre_sum[m] >= t) or (self.pre_sum[m-1] < t <= self.pre_sum[m]):
                return m
            
            if self.pre_sum[m] < t:
                l = m + 1
            else:
                r = m - 1

    
    def pick_point(self, idx):
        rec = self.rects[idx]
        
        x = random.randint(rec[0], rec[2])
        y = random.randint(rec[1], rec[3])
        
        return [x, y]
    

    def pick(self):
        """
        :rtype: List[int]
        """
        rec_idx = self.pick_rectangle()
        return self.pick_point(rec_idx)
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()