class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)        
        left, right = 0, sum(nums)
        
        for i in range(nums_len):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]
            
        return -1
        s