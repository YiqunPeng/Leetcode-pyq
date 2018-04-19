class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums_len = len(nums)
        
        if nums_len == 0:
            if upper - lower == 0:
                return [str(upper)]
            else:
                return [str(lower) + '->' + str(upper)]
     
        ans = []
        
        if nums[0] - lower == 1:
            ans.append(str(lower))
        elif nums[0] - lower > 1:
            ans.append(str(lower) + '->' + str(nums[0]-1))
        
        for i in range(nums_len-1):
            if 0 <= nums[i+1] - nums[i] <= 1: continue
            if nums[i+1] - nums[i] == 2: 
                ans.append(str(nums[i]+1))
            else:   
                ans.append(str(nums[i]+1) + '->' + str(nums[i+1]-1))
                
        if upper - nums[-1] == 1:
            ans.append(str(upper))
        elif upper - nums[-1] > 1:
            ans.append(str(nums[-1]+1) + '->' + str(upper))
                
        return ans
        
            