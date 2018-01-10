class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        dp_1 = nums[0]
        dp = 0
        n = len(nums)
        
        for i in range(1, n):
            if dp_1 <= 0:
                dp = nums[i]
            else:
                dp = dp_1 + nums[i]
            if ans < dp:
                ans = dp
            dp_1 = dp
            
        return ans