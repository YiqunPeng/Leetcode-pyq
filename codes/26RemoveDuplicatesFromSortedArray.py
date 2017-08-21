class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return len(nums)
        
        ans = 1
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i-1]:
                ans += 1
        
        pos = 0
        for i in xrange(1, len(nums)):
            if nums[pos] < nums[i]:
                pos += 1
                nums[pos] = nums[i]

        return ans
