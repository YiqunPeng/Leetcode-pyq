class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [0] + nums
        for i in xrange(len(nums)):
            index = abs(nums[i])
            nums[index] = -abs(nums[index])
        ans = []
        for i in xrange(1, len(nums)):
            if nums[i] > 0:
                ans.append(i)
        
        return ans