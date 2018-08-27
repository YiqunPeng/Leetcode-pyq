class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        n = len(nums) 
        dp = [[-sys.maxsize, sys.maxsize] for i in range(n + 1)]
        
        ans = -sys.maxsize
        
        for i in range(1, n + 1):
            if nums[i-1] == 0:
                dp[i] = [0, 0]
            elif nums[i-1] > 0:
                dp[i][0] = max(dp[i-1][0] * nums[i-1], nums[i-1])
                dp[i][1] = min(dp[i-1][1] * nums[i-1], nums[i-1])
            else:
                dp[i][0] = max(dp[i-1][1] * nums[i-1], nums[i-1])
                dp[i][1] = min(dp[i-1][0] * nums[i-1], nums[i-1])
        
            ans = max(ans, dp[i][0])
        
        return ans