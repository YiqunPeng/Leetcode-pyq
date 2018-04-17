class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        length = 0
        pre = nums[0] - 1
        cnt = 0
        
        for i in range(len(nums)):
            if nums[i] == pre and cnt == 2:
                continue
            elif nums[i] == pre and cnt < 2:
                cnt += 1
                length += 1
                nums[length-1] = nums[i]
            elif nums[i] != pre:
                length += 1
                cnt = 1
                nums[length-1] = nums[i]
                pre = nums[i]
                
        return length
        
        
        