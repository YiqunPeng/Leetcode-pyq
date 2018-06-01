class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                pos = i
                break
        
        min_pos = pos
        if pos <= 0: 
            pos = 0
        else:
            for i in range(pos, len(nums)):
                if nums[i] > nums[pos-1] and nums[i] < nums[min_pos]:
                    min_pos = i      
            nums[pos-1], nums[min_pos] = nums[min_pos], nums[pos-1]
                
        nums[pos:] = sorted(nums[pos:])
