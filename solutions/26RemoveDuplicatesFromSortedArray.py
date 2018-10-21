class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        
        for num in nums:
            if pos < 1 or num != nums[pos - 1]:
                nums[pos] = num
                pos += 1

        return pos