class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def range_sum(i, j):
            if i == 0: 
                return pre_sum[j]
            else:
                return pre_sum[j] - pre_sum[i-1]

        n = len(nums)
        dp = [[0] * n for i in range(n)]
        
        pre_sum = [0] * n
        pre_sum[0] = nums[0]
        for i in range(1, n):
            pre_sum[i] = pre_sum[i-1] + nums[i]
        
        for i in range(n):
            dp[i][i] = nums[i]
        for j in range(1, n):
            for i in range(n):
                if i + j >= n: break
                dp[i][i+j] = max(nums[i] + range_sum(i+1, i+j) - dp[i+1][i+j], nums[i+j] + range_sum(i, i+j-1) - dp[i][i+j-1])
        
        if dp[0][-1] * 2 >= pre_sum[-1]:
            return True
        else:
            return False