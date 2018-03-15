class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        dp = [[[0,0] for i in range(N)] for j in range(N)]
        nums_sum = sum(nums)
        
        for i in range(N):
            dp[i][i][0] = nums[i]
            
        for j in range(1, N):
            for i in range(j - 1 , -1, -1):
                dp[i][j][0] = max(nums[i] + dp[i+1][j][1], nums[j] + dp[i][j-1][1])
                dp[i][j][1] = sum(nums[i:j+1]) - dp[i][j][0]
                        
        if dp[0][N-1][0] >= dp[0][N-1][1]:
            return True
        else:
            return False