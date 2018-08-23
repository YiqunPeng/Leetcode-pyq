class Solution:
    # dp
    # time: O(n * m) n -- number of nums, m -- sum of nums
    # space: O(n * m)
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return True
        
        nums_sum = sum(nums)
        if nums_sum % 2 != 0: return False 
        sub_sum = nums_sum // 2
        
        n = len(nums)
        dp = [[False] * (sub_sum + 1) for i in range(n+1)]
        dp[0][0] = True
        
        for i in range(1, n + 1):
            dp[i][0] = True
            for j in range(sub_sum + 1):
                dp[i][j] = dp[i][j] or dp[i-1][j] or (dp[i-1][j-nums[i-1]] if j >= nums[i-1] else False)
        
            if dp[i][sub_sum]: return True
            
        return False