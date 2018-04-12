class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len == 0: return 0
        if nums_len == 1: return nums[0]
        dp = [0] * nums_len
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, nums_len):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            
        return dp[nums_len - 1]
        