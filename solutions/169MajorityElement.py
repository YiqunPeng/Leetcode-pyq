class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = nums[0]
        cnt = 1
        
        for i in range(1, len(nums)):
            if cnt == 0:
                major = nums[i]
                cnt = 1
                continue
            
            if nums[i] == major:
                cnt += 1
            else:
                cnt -= 1
           
        return major    