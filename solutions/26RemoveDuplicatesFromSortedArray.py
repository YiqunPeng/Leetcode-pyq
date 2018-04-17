class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        length = 0
        pre = nums[0] - 1
        
        for i in range(len(nums)):
            if nums[i] == pre: 
                continue
            else:
                length += 1
                nums[length-1] = nums[i]
                pre = nums[i]
        
        return length
            