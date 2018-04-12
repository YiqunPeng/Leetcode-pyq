class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        
        max_len = 0
        
        for i in range(n):
            if i <= max_len:
                max_len = max(max_len, i + nums[i])
            else:
                return False
            if max_len >= n-1:
                return True

        return True if max_len < n-1 else False