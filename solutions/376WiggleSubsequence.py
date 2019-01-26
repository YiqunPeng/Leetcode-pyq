class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        up, down = 1, 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = max(up, down + 1)
            elif nums[i] < nums[i-1]:
                down = max(down, up + 1)
        
        return max(up, down)