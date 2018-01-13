class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """        
        nums_len = len(nums)
        for i in range(1, nums_len):
            nums[i] += nums[i-1]
        
        ans = -sys.maxsize
        
        for i in range(nums_len-1, k-2, -1):
            if i - k < 0:
                ans = max(ans, nums[i])
            else:
                ans = max(ans, nums[i]-nums[i-k])
        
        return ans / float(k)