class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        
        for i in xrange(len(nums)):
            pos = abs(nums[i]) - 1
            if nums[pos] > 0:
                nums[pos] = -nums[pos]
            else:
                ans.append(abs(nums[i]))
        
        return ans