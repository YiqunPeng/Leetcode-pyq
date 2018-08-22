class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        
        n = len(nums)
        nums.sort()
        
        dp = [[]] * n
        ans = []
        
        for i in range(n):  
            
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[j]]

            if len(dp[i]) + 1 > len(ans):
                ans = dp[i] + [nums[i]]

        return ans