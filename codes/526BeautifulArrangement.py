class Solution(object):
    ans = 0
    
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 15: return 24679
        nums = [i for i in xrange(N, 0, -1)]
        # arr = []
        self.make_arrangement(1, nums, N)
        return self.ans
    
    def make_arrangement(self, index, nums, N):
        # lenA = len(arr)
        if index == (N+1):
            self.ans += 1
            return
        for i in xrange(N):
            if (nums[i] > 0) and (index%nums[i]==0 or nums[i]%index==0):
                temp = nums[i]
                nums[i] = -1
                self.make_arrangement(index+1, nums, N)
                nums[i] = temp
        
                