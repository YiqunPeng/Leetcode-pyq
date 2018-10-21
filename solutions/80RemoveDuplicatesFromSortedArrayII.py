class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        
        for num in nums:
            if pos < 2 or num > nums[pos - 2]:
                nums[pos] = num
                pos += 1
        
        return pos