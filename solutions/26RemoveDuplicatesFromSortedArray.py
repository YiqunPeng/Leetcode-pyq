class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0 or n == 1: return n
        
        pos = 0
        for num in nums:
            if pos == 0 or num != nums[pos - 1]:
                nums[pos] = num
                pos += 1
                
        return pos