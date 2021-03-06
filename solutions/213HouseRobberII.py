class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(nums):
            if len(nums) == 1: return nums[0]
            if len(nums) == 0: return 0
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[1], nums[0])
            
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
            return dp[-1]
        
        if len(nums) == 1: return nums[0]
        if len(nums) == 0: return 0
        
        return max(helper(nums[0:-1]), helper(nums[1:]))